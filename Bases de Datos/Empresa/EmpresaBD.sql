PGDMP     5                 	    y           Empresa    14.0    14.0                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    17471    Empresa    DATABASE     f   CREATE DATABASE "Empresa" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Mexico.1252';
    DROP DATABASE "Empresa";
                postgres    false            �            1259    17497    departamento    TABLE     �   CREATE TABLE public.departamento (
    numd integer NOT NULL,
    nomd character(20),
    nssemp integer,
    fechadir date,
    nump integer
);
     DROP TABLE public.departamento;
       public         heap    postgres    false            �            1259    17487    dependiente    TABLE     �   CREATE TABLE public.dependiente (
    apa character(15) NOT NULL,
    ama character(15),
    nombre character(15) NOT NULL,
    sexo character(15),
    parentesco character(15),
    fechanac date,
    nssemp integer NOT NULL
);
    DROP TABLE public.dependiente;
       public         heap    postgres    false            �            1259    17477    empleado    TABLE     -  CREATE TABLE public.empleado (
    apa character(15) NOT NULL,
    ama character(15),
    nombre character(15) NOT NULL,
    nss integer NOT NULL,
    direccion character(40),
    salario integer,
    sexo character(15),
    fechanac date,
    nsssup integer NOT NULL,
    numdads integer NOT NULL
);
    DROP TABLE public.empleado;
       public         heap    postgres    false            �            1259    17522    lugar    TABLE     g   CREATE TABLE public.lugar (
    nssemp integer NOT NULL,
    nump integer NOT NULL,
    hrs integer
);
    DROP TABLE public.lugar;
       public         heap    postgres    false            �            1259    17472    proyecto    TABLE     �   CREATE TABLE public.proyecto (
    nump integer NOT NULL,
    nomp character(20),
    lugar character(50),
    numdc integer NOT NULL
);
    DROP TABLE public.proyecto;
       public         heap    postgres    false            �            1259    17537 
   trabaja_en    TABLE     a   CREATE TABLE public.trabaja_en (
    numd integer NOT NULL,
    lugaru character(30) NOT NULL
);
    DROP TABLE public.trabaja_en;
       public         heap    postgres    false                      0    17497    departamento 
   TABLE DATA           J   COPY public.departamento (numd, nomd, nssemp, fechadir, nump) FROM stdin;
    public          postgres    false    212   �#                 0    17487    dependiente 
   TABLE DATA           [   COPY public.dependiente (apa, ama, nombre, sexo, parentesco, fechanac, nssemp) FROM stdin;
    public          postgres    false    211   $                 0    17477    empleado 
   TABLE DATA           n   COPY public.empleado (apa, ama, nombre, nss, direccion, salario, sexo, fechanac, nsssup, numdads) FROM stdin;
    public          postgres    false    210   �$                 0    17522    lugar 
   TABLE DATA           2   COPY public.lugar (nssemp, nump, hrs) FROM stdin;
    public          postgres    false    213   �%                 0    17472    proyecto 
   TABLE DATA           <   COPY public.proyecto (nump, nomp, lugar, numdc) FROM stdin;
    public          postgres    false    209   8&                 0    17537 
   trabaja_en 
   TABLE DATA           2   COPY public.trabaja_en (numd, lugaru) FROM stdin;
    public          postgres    false    214   �&       t           2606    17491    dependiente cevdepen 
   CONSTRAINT     c   ALTER TABLE ONLY public.dependiente
    ADD CONSTRAINT cevdepen PRIMARY KEY (apa, nombre, nssemp);
 >   ALTER TABLE ONLY public.dependiente DROP CONSTRAINT cevdepen;
       public            postgres    false    211    211    211            v           2606    17501    departamento cvedepa 
   CONSTRAINT     T   ALTER TABLE ONLY public.departamento
    ADD CONSTRAINT cvedepa PRIMARY KEY (numd);
 >   ALTER TABLE ONLY public.departamento DROP CONSTRAINT cvedepa;
       public            postgres    false    212            r           2606    17481    empleado cveempleado 
   CONSTRAINT     S   ALTER TABLE ONLY public.empleado
    ADD CONSTRAINT cveempleado PRIMARY KEY (nss);
 >   ALTER TABLE ONLY public.empleado DROP CONSTRAINT cveempleado;
       public            postgres    false    210            x           2606    17526    lugar cvelugar 
   CONSTRAINT     V   ALTER TABLE ONLY public.lugar
    ADD CONSTRAINT cvelugar PRIMARY KEY (nssemp, nump);
 8   ALTER TABLE ONLY public.lugar DROP CONSTRAINT cvelugar;
       public            postgres    false    213    213            p           2606    17476    proyecto cveproy 
   CONSTRAINT     P   ALTER TABLE ONLY public.proyecto
    ADD CONSTRAINT cveproy PRIMARY KEY (nump);
 :   ALTER TABLE ONLY public.proyecto DROP CONSTRAINT cveproy;
       public            postgres    false    209            z           2606    17541    trabaja_en cvetrabaja 
   CONSTRAINT     ]   ALTER TABLE ONLY public.trabaja_en
    ADD CONSTRAINT cvetrabaja PRIMARY KEY (numd, lugaru);
 ?   ALTER TABLE ONLY public.trabaja_en DROP CONSTRAINT cvetrabaja;
       public            postgres    false    214    214            ~           2606    17492    dependiente cvenssemp    FK CONSTRAINT     w   ALTER TABLE ONLY public.dependiente
    ADD CONSTRAINT cvenssemp FOREIGN KEY (nssemp) REFERENCES public.empleado(nss);
 ?   ALTER TABLE ONLY public.dependiente DROP CONSTRAINT cvenssemp;
       public          postgres    false    211    3186    210                       2606    17502    departamento cvenssemp    FK CONSTRAINT     �   ALTER TABLE ONLY public.departamento
    ADD CONSTRAINT cvenssemp FOREIGN KEY (nssemp) REFERENCES public.empleado(nss) ON DELETE SET DEFAULT;
 @   ALTER TABLE ONLY public.departamento DROP CONSTRAINT cvenssemp;
       public          postgres    false    212    3186    210            �           2606    17527    lugar cvenssemp    FK CONSTRAINT     q   ALTER TABLE ONLY public.lugar
    ADD CONSTRAINT cvenssemp FOREIGN KEY (nssemp) REFERENCES public.empleado(nss);
 9   ALTER TABLE ONLY public.lugar DROP CONSTRAINT cvenssemp;
       public          postgres    false    3186    210    213            �           2606    17542    trabaja_en cvenumd    FK CONSTRAINT     w   ALTER TABLE ONLY public.trabaja_en
    ADD CONSTRAINT cvenumd FOREIGN KEY (numd) REFERENCES public.departamento(numd);
 <   ALTER TABLE ONLY public.trabaja_en DROP CONSTRAINT cvenumd;
       public          postgres    false    212    3190    214            }           2606    17517    empleado cvenumdads    FK CONSTRAINT     {   ALTER TABLE ONLY public.empleado
    ADD CONSTRAINT cvenumdads FOREIGN KEY (numdads) REFERENCES public.departamento(numd);
 =   ALTER TABLE ONLY public.empleado DROP CONSTRAINT cvenumdads;
       public          postgres    false    212    210    3190            {           2606    17512    proyecto cvenumdc    FK CONSTRAINT     w   ALTER TABLE ONLY public.proyecto
    ADD CONSTRAINT cvenumdc FOREIGN KEY (numdc) REFERENCES public.departamento(numd);
 ;   ALTER TABLE ONLY public.proyecto DROP CONSTRAINT cvenumdc;
       public          postgres    false    3190    209    212            �           2606    17507    departamento cvenump    FK CONSTRAINT     u   ALTER TABLE ONLY public.departamento
    ADD CONSTRAINT cvenump FOREIGN KEY (nump) REFERENCES public.proyecto(nump);
 >   ALTER TABLE ONLY public.departamento DROP CONSTRAINT cvenump;
       public          postgres    false    212    209    3184            �           2606    17532    lugar cvenump    FK CONSTRAINT     n   ALTER TABLE ONLY public.lugar
    ADD CONSTRAINT cvenump FOREIGN KEY (nump) REFERENCES public.proyecto(nump);
 7   ALTER TABLE ONLY public.lugar DROP CONSTRAINT cvenump;
       public          postgres    false    213    209    3184            |           2606    17482    empleado cvesup    FK CONSTRAINT     q   ALTER TABLE ONLY public.empleado
    ADD CONSTRAINT cvesup FOREIGN KEY (nsssup) REFERENCES public.empleado(nss);
 9   ALTER TABLE ONLY public.empleado DROP CONSTRAINT cvesup;
       public          postgres    false    210    3186    210               �   x�mʻ�0���~��@P�K.;B�v	4C�BQS�� ��d�{�ֶ�Gn���I/p�8x]���_e.k͖B {��.��^�Һ���W�zB!FD��E�:��HHtX�[�չNy��A�:��㎙? �/         �   x���A�0���)�@M���@		J���L��h�"No1�W�3�������)Y�*vGW'�kk���s�PRI!3��;���"��m����ŜI�Cf�3@���7�Wd�[�6��
IBIP!X��JO1y��D���sq� �R��M�ot���A�Ea����Y	           x�u��n� ���� ���O���Z��\66��T`���/��8�����4ëAG6�4g�Z�̻�,�i	������!�XVD
!�c;Z��r��jrY��s}�<�1Xt�_�I����`�ir�F�Yt�AK����@�g���E�1ݼ������C[�U��K1�
*�5��=�����fEi�X����]P�!��:�V�����6�q�����:�}�7A�$r��E�9W�O]f�Z�\�)�P����o���         8   x�ʹ  �X*�A?��6�9I��C�2"Z���M��̄�����s�Z�
E         s   x�355�t,(P@��i�əy������	����Pc^Ub1�l@fq��)	�454�277�H,H�I-�Dv�@C�434㲰��tO-.���C��D����\1z\\\ ��7(         F   x�3426��O�L��KT��MM92��Lq(�134��1ĭ����&�	�C�#����qqq ��=     