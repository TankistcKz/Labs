import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import java.util.Properties
import java.io.File
import org.gradle.api.DefaultTask
import org.gradle.api.provider.Property
import org.gradle.api.tasks.Input
import org.gradle.api.tasks.TaskAction
import org.gradle.api.file.DirectoryProperty
import org.gradle.api.tasks.InputDirectory
import org.gradle.api.tasks.PathSensitive
import org.gradle.api.tasks.PathSensitivity

plugins {
	id("java")
    application
    id("com.gradleup.shadow") version "9.0.0-beta4"
}

repositories {
    // Use Maven Central for resolving dependencies.
    mavenCentral()
}

dependencies {
    implementation("org.apache.commons:commons-lang3:3.14.0")
    
    implementation("ch.qos.logback:logback-classic:1.4.14")
    implementation("org.slf4j:slf4j-api:2.0.9")
    
    testImplementation("org.junit.jupiter:junit-jupiter-api:5.10.0")
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine:5.10.0")
    testImplementation("org.junit.jupiter:junit-jupiter-params:5.10.0")
    
    testRuntimeOnly("org.junit.platform:junit-platform-launcher:1.10.0")
}

// Apply a specific Java toolchain to ease working on different environments.
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

application {
    // Define the main class for the application.
    mainClass = "org.example.Main"
}

tasks.named<Test>("test") {
    // Use JUnit Platform for unit tests.
    useJUnitPlatform()
}

tasks.shadowJar {
manifest {
        attributes["Main-Class"] = "org.example.Main"
    }
    
    archiveBaseName.set("Gradle_Lab")
    archiveClassifier.set("")
    archiveVersion.set("")
}

abstract class GenerateBuildPassportTask : DefaultTask() {

    @get:Input
    abstract val projectName: Property<String>

    @get:InputDirectory
    @get:PathSensitive(PathSensitivity.RELATIVE)
    abstract val projectDir: DirectoryProperty

    @TaskAction
    fun generate() {
        val properties = Properties()

        val userName = System.getenv("USER") ?: System.getenv("USERNAME") ?: "unknown"
        properties.setProperty("build.user", userName)

        properties.setProperty("build.os", System.getProperty("os.name"))
        properties.setProperty("build.java.version", System.getProperty("java.version"))

        val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")
        val buildTime = LocalDateTime.now()
        properties.setProperty("build.time", buildTime.format(formatter))

        properties.setProperty("build.message", "Сборка проекта ${projectName.get()}")

        val outputDir = projectDir.get().asFile.toPath().resolve("src/main/resources").toFile()
        outputDir.mkdirs()

        val file = File(outputDir, "build-passport.properties")
        file.outputStream().use { properties.store(it, "Build Passport") }

        println("Build passport generated: ${file.absolutePath}")
        println("Содержит: user=${userName}, os=${System.getProperty("os.name")}, time=${buildTime.format(formatter)}")
    }
}

tasks.register<GenerateBuildPassportTask>("generateBuildPassport") {
    group = "Custom"
    description = "Генерирует файл build-passport.properties с информацией о сборке"

    projectName.set(project.name)
    projectDir.set(project.layout.projectDirectory)
}

tasks.named("compileJava") {
    dependsOn(tasks.named("generateBuildPassport"))
}

tasks.named("processResources") {
	dependsOn(tasks.named("generateBuildPassport"))
}

tasks.named("processTestResources") {
    mustRunAfter(tasks.named("generateBuildPassport"))
}
