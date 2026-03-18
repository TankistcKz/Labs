package org.example.config;

import org.example.service.*;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.ComponentScan;

@Configuration
@ComponentScan("org.example")
public class AppConfig {
    public EmailService emailService() {
        return new EmailService();
    }

    public SmsService smsService() {
        return new SmsService();
    }

    // public NotificationManager notificationManager() {
    //     return new NotificationManager(emailService());
    //     // return new NotificationManager(smsService());
    //     // return new NotificationManager(pushService());
    // }  
      
    // @Bean
    // public PushService pushService() {
    //     return new PushService();
    // }
}
