PGDMP     	    !                y            Mixup    14.0    14.0 >    \           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ]           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ^           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            _           1262    28614    Mixup    DATABASE     d   CREATE DATABASE "Mixup" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Mexico.1252';
    DROP DATABASE "Mixup";
                postgres    false            �            1255    28751    bono()    FUNCTION     �  CREATE FUNCTION public.bono() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
begin
	update bono
	set nssven= (select nssVen
				 from empleadoVentas
				 where "MontoTotal"=(select max("MontoTotal")
				 					 from empleadoVentas))
	,"MontoTotal" =(select "MontoTotal"
					   from empleadoVentas
				  	   where "MontoTotal"=(select max("MontoTotal")
				 					  	   from empleadoVentas))
	,bono =(select ("MontoTotal"*.10) as Bono
			   from empleadoVentas
			   where "MontoTotal"=(select max("MontoTotal")
				 				   from empleadoVentas))
	where nssven!=(select nssven
				  from empleadoVentas
				  where "MontoTotal"=(select max("MontoTotal")
				 					  from empleadoVentas));
	return new;
end $$;
    DROP FUNCTION public.bono();
       public          postgres    false            �            1255    28749    ventas()    FUNCTION     �   CREATE FUNCTION public.ventas() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
begin
	update empleadoVentas
	set "MontoTotal"="MontoTotal"+new.montoV
	where nssVen = new.nssVen;
	return new;
end $$;
    DROP FUNCTION public.ventas();
       public          postgres    false            �            1259    28709    actores    TABLE     i   CREATE TABLE public.actores (
    codigopvid integer NOT NULL,
    nombreactor character(30) NOT NULL
);
    DROP TABLE public.actores;
       public         heap    postgres    false            �            1259    28744    bono    TABLE     ]   CREATE TABLE public.bono (
    nssven integer,
    "MontoTotal" numeric,
    bono numeric
);
    DROP TABLE public.bono;
       public         heap    postgres    false            �            1259    28626 
   cfrecuente    TABLE     d   CREATE TABLE public.cfrecuente (
    codigocf integer NOT NULL,
    cantcompras integer NOT NULL
);
    DROP TABLE public.cfrecuente;
       public         heap    postgres    false            �            1259    28620    cliente    TABLE     �   CREATE TABLE public.cliente (
    codigoc integer DEFAULT 0 NOT NULL,
    nombrep character(15),
    appat character(15),
    apmat character(15),
    edad integer
);
    DROP TABLE public.cliente;
       public         heap    postgres    false            �            1259    28615    empleado    TABLE     �   CREATE TABLE public.empleado (
    nss integer NOT NULL,
    nombrep character(15),
    appat character(15),
    apmat character(15),
    fnac date,
    direccion character(15),
    salario numeric(10,2),
    sexo character(1)
);
    DROP TABLE public.empleado;
       public         heap    postgres    false            �            1259    28739    empleadoventas    TABLE     U   CREATE TABLE public.empleadoventas (
    nssven integer,
    "MontoTotal" numeric
);
 "   DROP TABLE public.empleadoventas;
       public         heap    postgres    false            �            1259    28719    libro    TABLE     �   CREATE TABLE public.libro (
    codigopl integer NOT NULL,
    pags integer,
    autor character(30),
    editorial character(30)
);
    DROP TABLE public.libro;
       public         heap    postgres    false            �            1259    28689    musica    TABLE     n   CREATE TABLE public.musica (
    codigopm integer NOT NULL,
    artista character(30),
    ntracks integer
);
    DROP TABLE public.musica;
       public         heap    postgres    false            �            1259    28669    proddescuento    TABLE     j   CREATE TABLE public.proddescuento (
    codigop integer NOT NULL,
    descuento numeric(10,2) NOT NULL
);
 !   DROP TABLE public.proddescuento;
       public         heap    postgres    false            �            1259    28679 
   prodpremio    TABLE     d   CREATE TABLE public.prodpremio (
    codigop integer NOT NULL,
    premio character(30) NOT NULL
);
    DROP TABLE public.prodpremio;
       public         heap    postgres    false            �            1259    28663    producto    TABLE     !  CREATE TABLE public.producto (
    codigop integer DEFAULT 0 NOT NULL,
    nombrepr character(20) NOT NULL,
    precio numeric(10,2),
    pasillo character(15) NOT NULL,
    tipo_p character(2) NOT NULL,
    formato character(15) NOT NULL,
    aniopublic date,
    genero character(15)
);
    DROP TABLE public.producto;
       public         heap    postgres    false            �            1259    28636    tarjeta    TABLE     e   CREATE TABLE public.tarjeta (
    codigocf integer DEFAULT 0 NOT NULL,
    fechacad date NOT NULL
);
    DROP TABLE public.tarjeta;
       public         heap    postgres    false            �            1259    28647    venta    TABLE     �   CREATE TABLE public.venta (
    numventa integer DEFAULT 0 NOT NULL,
    nssven integer NOT NULL,
    codigoc integer NOT NULL,
    montov numeric(10,2)
);
    DROP TABLE public.venta;
       public         heap    postgres    false            �            1259    28699    video    TABLE     u   CREATE TABLE public.video (
    codigopv integer NOT NULL,
    "duraciónmin" integer,
    director character(30)
);
    DROP TABLE public.video;
       public         heap    postgres    false            �            1259    28729 
   videojuego    TABLE     �   CREATE TABLE public.videojuego (
    codigopvd integer NOT NULL,
    desarrolladopor character(30),
    plataforma character(25)
);
    DROP TABLE public.videojuego;
       public         heap    postgres    false            U          0    28709    actores 
   TABLE DATA           :   COPY public.actores (codigopvid, nombreactor) FROM stdin;
    public          postgres    false    219   	H       Y          0    28744    bono 
   TABLE DATA           :   COPY public.bono (nssven, "MontoTotal", bono) FROM stdin;
    public          postgres    false    223   {H       M          0    28626 
   cfrecuente 
   TABLE DATA           ;   COPY public.cfrecuente (codigocf, cantcompras) FROM stdin;
    public          postgres    false    211   �H       L          0    28620    cliente 
   TABLE DATA           G   COPY public.cliente (codigoc, nombrep, appat, apmat, edad) FROM stdin;
    public          postgres    false    210   �H       K          0    28615    empleado 
   TABLE DATA           ^   COPY public.empleado (nss, nombrep, appat, apmat, fnac, direccion, salario, sexo) FROM stdin;
    public          postgres    false    209   vI       X          0    28739    empleadoventas 
   TABLE DATA           >   COPY public.empleadoventas (nssven, "MontoTotal") FROM stdin;
    public          postgres    false    222   �J       V          0    28719    libro 
   TABLE DATA           A   COPY public.libro (codigopl, pags, autor, editorial) FROM stdin;
    public          postgres    false    220   �J       S          0    28689    musica 
   TABLE DATA           <   COPY public.musica (codigopm, artista, ntracks) FROM stdin;
    public          postgres    false    217   9K       Q          0    28669    proddescuento 
   TABLE DATA           ;   COPY public.proddescuento (codigop, descuento) FROM stdin;
    public          postgres    false    215   �K       R          0    28679 
   prodpremio 
   TABLE DATA           5   COPY public.prodpremio (codigop, premio) FROM stdin;
    public          postgres    false    216   �K       P          0    28663    producto 
   TABLE DATA           k   COPY public.producto (codigop, nombrepr, precio, pasillo, tipo_p, formato, aniopublic, genero) FROM stdin;
    public          postgres    false    214   �K       N          0    28636    tarjeta 
   TABLE DATA           5   COPY public.tarjeta (codigocf, fechacad) FROM stdin;
    public          postgres    false    212   DM       O          0    28647    venta 
   TABLE DATA           B   COPY public.venta (numventa, nssven, codigoc, montov) FROM stdin;
    public          postgres    false    213   xM       T          0    28699    video 
   TABLE DATA           C   COPY public.video (codigopv, "duraciónmin", director) FROM stdin;
    public          postgres    false    218   �M       W          0    28729 
   videojuego 
   TABLE DATA           L   COPY public.videojuego (codigopvd, desarrolladopor, plataforma) FROM stdin;
    public          postgres    false    221   N       �           2606    28713    actores cveactores 
   CONSTRAINT     e   ALTER TABLE ONLY public.actores
    ADD CONSTRAINT cveactores PRIMARY KEY (codigopvid, nombreactor);
 <   ALTER TABLE ONLY public.actores DROP CONSTRAINT cveactores;
       public            postgres    false    219    219            �           2606    28630    cfrecuente cvecf 
   CONSTRAINT     T   ALTER TABLE ONLY public.cfrecuente
    ADD CONSTRAINT cvecf PRIMARY KEY (codigocf);
 :   ALTER TABLE ONLY public.cfrecuente DROP CONSTRAINT cvecf;
       public            postgres    false    211            �           2606    28625    cliente cvecodigoc 
   CONSTRAINT     U   ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cvecodigoc PRIMARY KEY (codigoc);
 <   ALTER TABLE ONLY public.cliente DROP CONSTRAINT cvecodigoc;
       public            postgres    false    210            �           2606    28619    empleado cveempleado 
   CONSTRAINT     S   ALTER TABLE ONLY public.empleado
    ADD CONSTRAINT cveempleado PRIMARY KEY (nss);
 >   ALTER TABLE ONLY public.empleado DROP CONSTRAINT cveempleado;
       public            postgres    false    209            �           2606    28723    libro cvelibro 
   CONSTRAINT     R   ALTER TABLE ONLY public.libro
    ADD CONSTRAINT cvelibro PRIMARY KEY (codigopl);
 8   ALTER TABLE ONLY public.libro DROP CONSTRAINT cvelibro;
       public            postgres    false    220            �           2606    28693    musica cvemusica 
   CONSTRAINT     T   ALTER TABLE ONLY public.musica
    ADD CONSTRAINT cvemusica PRIMARY KEY (codigopm);
 :   ALTER TABLE ONLY public.musica DROP CONSTRAINT cvemusica;
       public            postgres    false    217            �           2606    28673    proddescuento cvepd 
   CONSTRAINT     a   ALTER TABLE ONLY public.proddescuento
    ADD CONSTRAINT cvepd PRIMARY KEY (codigop, descuento);
 =   ALTER TABLE ONLY public.proddescuento DROP CONSTRAINT cvepd;
       public            postgres    false    215    215            �           2606    28683    prodpremio cvepp 
   CONSTRAINT     [   ALTER TABLE ONLY public.prodpremio
    ADD CONSTRAINT cvepp PRIMARY KEY (codigop, premio);
 :   ALTER TABLE ONLY public.prodpremio DROP CONSTRAINT cvepp;
       public            postgres    false    216    216            �           2606    28668    producto cveproducto 
   CONSTRAINT     W   ALTER TABLE ONLY public.producto
    ADD CONSTRAINT cveproducto PRIMARY KEY (codigop);
 >   ALTER TABLE ONLY public.producto DROP CONSTRAINT cveproducto;
       public            postgres    false    214            �           2606    28641    tarjeta cvetarjeta 
   CONSTRAINT     `   ALTER TABLE ONLY public.tarjeta
    ADD CONSTRAINT cvetarjeta PRIMARY KEY (fechacad, codigocf);
 <   ALTER TABLE ONLY public.tarjeta DROP CONSTRAINT cvetarjeta;
       public            postgres    false    212    212            �           2606    28652    venta cveventa 
   CONSTRAINT     c   ALTER TABLE ONLY public.venta
    ADD CONSTRAINT cveventa PRIMARY KEY (numventa, nssven, codigoc);
 8   ALTER TABLE ONLY public.venta DROP CONSTRAINT cveventa;
       public            postgres    false    213    213    213            �           2606    28703    video cvevideo 
   CONSTRAINT     R   ALTER TABLE ONLY public.video
    ADD CONSTRAINT cvevideo PRIMARY KEY (codigopv);
 8   ALTER TABLE ONLY public.video DROP CONSTRAINT cvevideo;
       public            postgres    false    218            �           2606    28733    videojuego cvevideojuego 
   CONSTRAINT     ]   ALTER TABLE ONLY public.videojuego
    ADD CONSTRAINT cvevideojuego PRIMARY KEY (codigopvd);
 B   ALTER TABLE ONLY public.videojuego DROP CONSTRAINT cvevideojuego;
       public            postgres    false    221            �           2620    28752    empleadoventas tr_bonototal    TRIGGER     y   CREATE TRIGGER tr_bonototal AFTER INSERT OR UPDATE ON public.empleadoventas FOR EACH ROW EXECUTE FUNCTION public.bono();
 4   DROP TRIGGER tr_bonototal ON public.empleadoventas;
       public          postgres    false    222    225            �           2620    28750    venta tr_ventascadaempleado    TRIGGER     {   CREATE TRIGGER tr_ventascadaempleado AFTER INSERT OR UPDATE ON public.venta FOR EACH ROW EXECUTE FUNCTION public.ventas();
 4   DROP TRIGGER tr_ventascadaempleado ON public.venta;
       public          postgres    false    213    224            �           2606    28658    venta cveclien    FK CONSTRAINT     �   ALTER TABLE ONLY public.venta
    ADD CONSTRAINT cveclien FOREIGN KEY (codigoc) REFERENCES public.cliente(codigoc) ON UPDATE CASCADE ON DELETE SET DEFAULT;
 8   ALTER TABLE ONLY public.venta DROP CONSTRAINT cveclien;
       public          postgres    false    210    213    3228            �           2606    28631    cfrecuente cvecliente    FK CONSTRAINT     �   ALTER TABLE ONLY public.cfrecuente
    ADD CONSTRAINT cvecliente FOREIGN KEY (codigocf) REFERENCES public.cliente(codigoc) ON UPDATE CASCADE ON DELETE SET DEFAULT;
 ?   ALTER TABLE ONLY public.cfrecuente DROP CONSTRAINT cvecliente;
       public          postgres    false    211    210    3228            �           2606    28642    tarjeta cvecodigoclient    FK CONSTRAINT     �   ALTER TABLE ONLY public.tarjeta
    ADD CONSTRAINT cvecodigoclient FOREIGN KEY (codigocf) REFERENCES public.cfrecuente(codigocf) ON UPDATE CASCADE ON DELETE SET DEFAULT;
 A   ALTER TABLE ONLY public.tarjeta DROP CONSTRAINT cvecodigoclient;
       public          postgres    false    212    3230    211            �           2606    28734    videojuego cvecodigojue    FK CONSTRAINT     �   ALTER TABLE ONLY public.videojuego
    ADD CONSTRAINT cvecodigojue FOREIGN KEY (codigopvd) REFERENCES public.producto(codigop);
 A   ALTER TABLE ONLY public.videojuego DROP CONSTRAINT cvecodigojue;
       public          postgres    false    221    3236    214            �           2606    28694    musica cvecodigomus    FK CONSTRAINT     �   ALTER TABLE ONLY public.musica
    ADD CONSTRAINT cvecodigomus FOREIGN KEY (codigopm) REFERENCES public.producto(codigop) ON UPDATE CASCADE ON DELETE SET DEFAULT;
 =   ALTER TABLE ONLY public.musica DROP CONSTRAINT cvecodigomus;
       public          postgres    false    3236    217    214            �           2606    28724    libro cvecodigopl    FK CONSTRAINT     y   ALTER TABLE ONLY public.libro
    ADD CONSTRAINT cvecodigopl FOREIGN KEY (codigopl) REFERENCES public.producto(codigop);
 ;   ALTER TABLE ONLY public.libro DROP CONSTRAINT cvecodigopl;
       public          postgres    false    3236    220    214            �           2606    28704    video cvecodigopv    FK CONSTRAINT     y   ALTER TABLE ONLY public.video
    ADD CONSTRAINT cvecodigopv FOREIGN KEY (codigopv) REFERENCES public.producto(codigop);
 ;   ALTER TABLE ONLY public.video DROP CONSTRAINT cvecodigopv;
       public          postgres    false    3236    218    214            �           2606    28714    actores cvecodigopvid    FK CONSTRAINT     }   ALTER TABLE ONLY public.actores
    ADD CONSTRAINT cvecodigopvid FOREIGN KEY (codigopvid) REFERENCES public.video(codigopv);
 ?   ALTER TABLE ONLY public.actores DROP CONSTRAINT cvecodigopvid;
       public          postgres    false    219    3244    218            �           2606    28674    proddescuento cveprod    FK CONSTRAINT     �   ALTER TABLE ONLY public.proddescuento
    ADD CONSTRAINT cveprod FOREIGN KEY (codigop) REFERENCES public.producto(codigop) ON UPDATE CASCADE ON DELETE SET DEFAULT;
 ?   ALTER TABLE ONLY public.proddescuento DROP CONSTRAINT cveprod;
       public          postgres    false    3236    215    214            �           2606    28684    prodpremio cveprod    FK CONSTRAINT     �   ALTER TABLE ONLY public.prodpremio
    ADD CONSTRAINT cveprod FOREIGN KEY (codigop) REFERENCES public.producto(codigop) ON UPDATE CASCADE ON DELETE SET DEFAULT;
 <   ALTER TABLE ONLY public.prodpremio DROP CONSTRAINT cveprod;
       public          postgres    false    3236    214    216            �           2606    28653    venta cveven    FK CONSTRAINT     �   ALTER TABLE ONLY public.venta
    ADD CONSTRAINT cveven FOREIGN KEY (nssven) REFERENCES public.empleado(nss) ON UPDATE CASCADE ON DELETE SET DEFAULT;
 6   ALTER TABLE ONLY public.venta DROP CONSTRAINT cveven;
       public          postgres    false    213    209    3226            U   b   x�3�t/�THM,JNU���9���2Su��R|�1x�*$���d&��c�`���������W�.Q��_�����V�������qqq ��$�      Y      x�3�4440�30 �@���+F��� 1��      M      x�34�44�24�&��F\1z\\\ (�3      L   �   x�34��*M�S@ N�ÛR��	ZrrF���d��D�/�K�@(��gd�eh��X��l_Pif2�7�����<�NNC.CcN׼����T���Ԝ$�9��S�2�KaB�F�\�&�.�y��9p�8����E������b���� w{@Z      K     x�]�AN�0EדS��l� YB�B���b3#b������m��S�b5u�g��?<����$X�V�����,��K&8�}��w[�w��Zp�D¹�/4�Nim�N�ye���9��;j��s��]'Gp��(Ѓ�$���"g��y�>N<�%�[���Nw	7^��u��	�m���b~31~��
�#�
�����m����Oö��J�5�n�6a2U,�P�5�N��B�1\(4��Tu�'G��@�y6��Ԩ�E���{Y$I��LzI      X   )   x�3�430�30�2�4�0L8 ,#��!��!����� �|      V   P   x�3�465�tO�/JOU�/*O��Q@�A�y)��
��ũ�
\f���f�nE�yU
މiى�j8�1MF����� �8�      S   9   x�3��N̫LUO-.Q�8�̹�8C*sR�tJ2R��RK�P��q��qqq ��|      Q      x�3�440�30������ +      R   6   x�3��/NN,R�M��/R(H�9�6�4'Q�,8��C"---��=... �S      P   F  x�}�Mj�0�ףS�
��k[��BRC�5�SQ�
�]ȱJ�������ݦ�VO���@�r��`N�R`y�!3��$N9#4!\��Ȼ;\��TY�W?���5gGt��ʱԳc£_� V��e�Ǝ�g�	;� ��eӖæ�]�
���O_���y�?��]��mH��W�	*@V�ċ"X*\�Z�ʝ7~�x0a/1����5��.��xv����(n'!�T����fU���i8e�]n�¹�n��Ds�����5�(����X����a�6�1%�P6'��z�`�[�����u
���Dx\o���u��9��N      N   $   x�34�4202�54�52�24�tA�=... _�a      O   >   x�=��	�0C���0A��t��?G[L
�<��KR$���*
�ݚL�N���u�����GD<[t=      T   ?   x�3�444�t�(�,.�/�H-R���I�S@\&��&F�nE�y�
.�E�I�y%
h�+F��� ��      W   :   x�3�t+��U�O+)O,JU@�I�
�f2\�a�9e�Z�Z�q�p��qqq ��z     