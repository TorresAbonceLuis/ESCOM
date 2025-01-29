#!/bin/sh                                                                                                             
#echo "/////////////////////////////////"
#echo "Ejercicio 3.1"
#ls -al /usr /tmp /noexiste >ls.sal 2>ls.err find 
#/tmp -print >find.sal 2>/dev/null
#echo "/////////////////////////////////"
#echo "Ejercicio 3.2"
#ls | tee salida | sort -r
#echo "/////////////////////////////////"
#echo "Ejercicio 4.1"
#echo "Variables de entorno:"
#echo "SHELL: $SHELL"
#echo "HOME: $HOME"
#echo "LOGNAME: $LONGNAME"
#echo "PATH: $PATH"
#echo "PAGER: $PAGER"
#echo "EDITOR: $EDITOR"
#echo "TERM: $TERM"
#echo "PS1: $PS1"
#echo "PS2: $PS2"
#echo "TZ: $TZ"
#echo "/////////////////////////////////"
#echo "Ejercicio 5.1"
#a=10
#echo "a: $a"
#b=$(expr 2 "*" 10)
#echo "b=2*10= $b"
#c=$(expr $a + \( $b / 2 \))
#echo "c=a+b/2= $c "
#c=$(expr 10 "*" \( 2 + 3 \))
#echo "c=(2+3)*10= $c"
#div=$(expr $c / 2)
#echo "div=c/2= $div"
#res=$(expr $b % $c)
#echo "res=b%c= $res"
#echo "/////////////////////////////////"
#echo "Ejercicio 5.2"
#practica1=/root/practica1.sh
#salida=/root/salida
#script=/root/script

#if [ -r root/practica1.sh -a -x root/practica1.sh ]; then
	#echo "Hola";
#fi
#if [ "$practica1" -ot "$salida" ] && [ "$practica1" -ot "$script" ]; then
	#echo "El archivo 1 es mas antiguo";
#fi
#if [ "$salida" -ot "$practica1" -a "$salida" -ot "$script" ]; then
	#echo "El archivo 2 es mas antiguo";
#fi
#if [ "$script" -ot "$practica1" -a "$script" -ot "$salida" ]; then 
	#echo "El archivo 3 es mas antiguo"
#fi
#if [ "$USER" -o "$script" ]; then
	#echo "Duenio del archivo: $USER" 
#fi

#if [ /root/practica1.sh -ot /root/script ]; then
#echo "cierto"
#else
#echo "Falso"
#fi

echo "/////////////////////////////////"
echo "Ejercicio 5.3"
if [ -z "$SHELL" -o "$SHELL" = "(none)" ];then echo "1"; fi
if [ -z "$HOME" -o "$HOME" = "(none)" ];then echo "2"; fi
if [ -z "$LOGNAME" -o "$LOGNAME" = "(none)" ];then echo "3"; fi
if [ -z "$PATH" -o "$PATH" = "(none)" ];then echo "4"; fi
if [ -z "$PAGER" -o "$PAGER" = "(none)" ];then echo "5"; fi
if [ -z "$EDITOR" -o "$EDITOR" = "(none)" ];then echo "6"; fi
if [ -z "$TERM" -o "$TERM" = "(none)" ];then echo "7"; fi
if [ -z "$PS1" -o "$PS1" = "(none)" ];then echo "8"; fi
if [ -z "$PS2" -o "$PS2" = "(none)" ];then echo "9"; fi
if [ -z "$TZ" -o "$TZ" = "(none)" ];then echo "10"; fi


#echo "/////////////////////////////////"
#echo "Ejercicio 7.2"
#if [ "$#" -eq "0" ]; then
	#echo "Sin argumentos"
#else
	#echo "numero de argumentos: $#"
	#echo "$*"
#fi
#echo "/////////////////////////////////"
#echo "Ejercicio 7.3"
#echo answer yes or no 
#read word
#case $word in 
	#yes | YES )
		#echo you answered yes ;;
	#no | NO )
		#echo you answered no ;;
#esac
#echo answer yes or no
#read word
#case $word in
	#[Yy]* )
		#echo you answered yes ;;
	#[Nn]* )
		#echo you answered no ;;
	#* ) 
		#echo you did not say yes or no ;;
#esac
#echo "/////////////////////////////////"
#echo "Ejercicio 7.4"
#read the /etc/password file
#use `cat /etc/passwd`, but spaces are treated like new lines
#therefore, change space into _

#for i in `tr ' ' '_' </etc/passwd` 
#do
	#set `echo $i | tr ':' ' '`
	#echo user: $1, UID: $3, Home Directory: $6
#done
#echo "/////////////////////////////////"
#echo "Ejercicio 7.5"
#for number in 1 2 3 4 5 6
#do
	#for letter in a b c d e f g 
	#do
		#case $number in
			#3 ) break;;
		#esac
		#echo $number $letter
	#done
#done
#echo "/////////////////////////////////"
#echo "Ejercicio 7.6"
#echo "Palabra: "
#read palabra
#for i in $palabra
#do
#	echo "$a" 
#done
#echo "Hola"
#echo "/////////////////////////////////"
#echo "Ejercicio 8.1"
#valor 
#echo -n "Dime tu nombre: "
#echo "$USER"
#read NOMBRE
#read -p "Dime tu nombre: " NOMBRE
#while FIS=: read usuario clave uid gid nombre ignorar 
#do
#	printf "%8s (%s)\n" $usuario $nombre
#done </etc/passwd
