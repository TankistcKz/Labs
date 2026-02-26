#!/bin/bash

print_help() {
    cat << EOF
Удаление файлов в текущем каталоге

Использование:
	$SCRIPT_NAME [опция] <имя_файла_или_шаблон>

Опции:
	-p	Режим шаблона: удалить ВСЕ файлы, содержащие указанную подстроку
	-h	Показать эту справку

EOF
}

if [ $# -lt 1 ] || [ $# -gt 2 ]; then
    print_help
    exit 1
fi


target=""
mode_p=false

case "$1" in
	-h)
		print_help
		exit 0
		;;
	-p)
		if [ -z "$2" ]; then
			print_help
			exit 1
		fi
		target="$2"
		mode_p=true
		;;
	*)
		target="$1"
		mode_p=false
		;;
esac

if [ $mode_p = true ]; then
	files_found=$(find . -maxdepth 1 -type f -name "*$target*")
	if [ -n "$files_found" ]; then
	    echo "$files_found" | while read file; do
	        rm "$file"
	    done
	else
	    echo "Файлы '$target' не найдены"
	    exit 1
	fi
else
	if [ -f "$target" ]; then
		rm "$target"
	else
		echo "Файлы '$target' не найдены"
		exit 1
	fi
fi
