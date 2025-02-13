PGDMP     $                 	    y        	   Viviendas    14.0    14.0                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    17547 	   Viviendas    DATABASE     h   CREATE DATABASE "Viviendas" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Mexico.1252';
    DROP DATABASE "Viviendas";
                postgres    false            �            1259    17903    dependiente    TABLE     �   CREATE TABLE public.dependiente (
    curp character(25) NOT NULL,
    parentesco character(20),
    curpdue character(25) NOT NULL
);
    DROP TABLE public.dependiente;
       public         heap    postgres    false            �            1259    17893    duenio    TABLE     e   CREATE TABLE public.duenio (
    curp character(25) NOT NULL,
    telefono character(10) NOT NULL
);
    DROP TABLE public.duenio;
       public         heap    postgres    false            �            1259    17878 	   habitante    TABLE       CREATE TABLE public.habitante (
    curp character(25) NOT NULL,
    rfc character(30),
    nombre character(20) NOT NULL,
    apa character(15) NOT NULL,
    ama character(15),
    genero character(15),
    rol character(15),
    nombremu character(30),
    direccion character(40)
);
    DROP TABLE public.habitante;
       public         heap    postgres    false            �            1259    17863 	   municipio    TABLE     G   CREATE TABLE public.municipio (
    nombremu character(30) NOT NULL
);
    DROP TABLE public.municipio;
       public         heap    postgres    false            �            1259    17868    vivienda    TABLE     c   CREATE TABLE public.vivienda (
    direccion character(40) NOT NULL,
    nombremu character(30)
);
    DROP TABLE public.vivienda;
       public         heap    postgres    false            	          0    17903    dependiente 
   TABLE DATA           @   COPY public.dependiente (curp, parentesco, curpdue) FROM stdin;
    public          postgres    false    213                    0    17893    duenio 
   TABLE DATA           0   COPY public.duenio (curp, telefono) FROM stdin;
    public          postgres    false    212   �                 0    17878 	   habitante 
   TABLE DATA           b   COPY public.habitante (curp, rfc, nombre, apa, ama, genero, rol, nombremu, direccion) FROM stdin;
    public          postgres    false    211   T                 0    17863 	   municipio 
   TABLE DATA           -   COPY public.municipio (nombremu) FROM stdin;
    public          postgres    false    209   �                 0    17868    vivienda 
   TABLE DATA           7   COPY public.vivienda (direccion, nombremu) FROM stdin;
    public          postgres    false    210   �       t           2606    17907    dependiente cvedepend 
   CONSTRAINT     ^   ALTER TABLE ONLY public.dependiente
    ADD CONSTRAINT cvedepend PRIMARY KEY (curp, curpdue);
 ?   ALTER TABLE ONLY public.dependiente DROP CONSTRAINT cvedepend;
       public            postgres    false    213    213            r           2606    17897    duenio cvedueño 
   CONSTRAINT     R   ALTER TABLE ONLY public.duenio
    ADD CONSTRAINT "cvedueño" PRIMARY KEY (curp);
 <   ALTER TABLE ONLY public.duenio DROP CONSTRAINT "cvedueño";
       public            postgres    false    212            p           2606    17882    habitante cvehabitante 
   CONSTRAINT     V   ALTER TABLE ONLY public.habitante
    ADD CONSTRAINT cvehabitante PRIMARY KEY (curp);
 @   ALTER TABLE ONLY public.habitante DROP CONSTRAINT cvehabitante;
       public            postgres    false    211            l           2606    17867    municipio cvemunicipio 
   CONSTRAINT     Z   ALTER TABLE ONLY public.municipio
    ADD CONSTRAINT cvemunicipio PRIMARY KEY (nombremu);
 @   ALTER TABLE ONLY public.municipio DROP CONSTRAINT cvemunicipio;
       public            postgres    false    209            n           2606    17872    vivienda cvevivienda 
   CONSTRAINT     Y   ALTER TABLE ONLY public.vivienda
    ADD CONSTRAINT cvevivienda PRIMARY KEY (direccion);
 >   ALTER TABLE ONLY public.vivienda DROP CONSTRAINT cvevivienda;
       public            postgres    false    210            y           2606    17908    dependiente cvecurpdue    FK CONSTRAINT     x   ALTER TABLE ONLY public.dependiente
    ADD CONSTRAINT cvecurpdue FOREIGN KEY (curpdue) REFERENCES public.duenio(curp);
 @   ALTER TABLE ONLY public.dependiente DROP CONSTRAINT cvecurpdue;
       public          postgres    false    213    212    3186            w           2606    17888    habitante cvedireccion    FK CONSTRAINT     �   ALTER TABLE ONLY public.habitante
    ADD CONSTRAINT cvedireccion FOREIGN KEY (direccion) REFERENCES public.vivienda(direccion);
 @   ALTER TABLE ONLY public.habitante DROP CONSTRAINT cvedireccion;
       public          postgres    false    210    211    3182            u           2606    17873    vivienda cvenombremu    FK CONSTRAINT     ~   ALTER TABLE ONLY public.vivienda
    ADD CONSTRAINT cvenombremu FOREIGN KEY (nombremu) REFERENCES public.municipio(nombremu);
 >   ALTER TABLE ONLY public.vivienda DROP CONSTRAINT cvenombremu;
       public          postgres    false    210    3180    209            v           2606    17883    habitante cvenombremu    FK CONSTRAINT        ALTER TABLE ONLY public.habitante
    ADD CONSTRAINT cvenombremu FOREIGN KEY (nombremu) REFERENCES public.municipio(nombremu);
 ?   ALTER TABLE ONLY public.habitante DROP CONSTRAINT cvenombremu;
       public          postgres    false    209    211    3180            x           2606    17898    duenio cvrcurp    FK CONSTRAINT     p   ALTER TABLE ONLY public.duenio
    ADD CONSTRAINT cvrcurp FOREIGN KEY (curp) REFERENCES public.habitante(curp);
 8   ALTER TABLE ONLY public.duenio DROP CONSTRAINT cvrcurp;
       public          postgres    false    211    3184    212            	   �   x���1� �ZN�	2~��2��H�M��I��wIF�ݙ7���FnE�O�_�O�K�P���K��FfKH�{��N�[4S U�{\r�M�SO
�r~=P2��M�zgs�O��׍���9�R�u�\�r� ��B���EGh��[iв�*���ɭD�         z   x�e�M� @�s
O`�f	�Kjw��9tg�o����P�>�%��ۅY4�
�Z��!��z�/"��T2zb�S>��'AB��u�K��qj��a4XLG��VL��Ȑ�� ���$          @  x���ߎ�0Ư�)x�	-E��ZT�Y�O&������q���f6
Ҩ��C{N=�wҘYЎf��|��uiʠmhY��/#�^n��`#O���Ę�C~,d���η�hmY�F6*�������f]�	l햟5X��� XÈ�y;��Bч�"Ţ�0=�C/���Z\�F����z�T	?���Ce��MQ�P���,c ����(ĝ��!d��
b���\�y�K~�&����R��}�E^���BKUʼ*��t�;T,K�r���xa��S���0Y�+�tT��w��{Y��S�+xQ
�%<M�)�U��۳�����R?\&c��6��(&��c�a�AՉM-E��1�J���W*���p�;��_"�����̭0���\�ބ��P�t��UBS��v
�(�vԂP���y'����������&�uJz��n��,pP���;q+��x�U�'���IL�v�% �DW�H��n��#�Gzy�G� �w\��O�v���l����˳Cn��<y�G��:N3�x za�LB�#�ź�g^�^�7�� �s/��o������         J   x�)�)�,�I�S���K�s
pI��$����&`�vMN,I-HMƪhxjUbFibNr~e~I�t� .	";         �   x�}�A
�0E��s�b��[�D
u�曆Z��L=�ѭif���{���AzC˷�$�Q�8�.-nȬM�sF��i�s�h��}t͇��eNv*pφzG��%����h!nr�����G�v�Z�{��6�����(�>�J9     