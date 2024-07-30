//Torres Abonce Luis Miguel
#include <iostream>
#include <cstring>

using namespace std;

struct Alumnos
{
    char nombre[50];
    long int boleta;
    float promedio;
}alumno[10];

int main()
{
    int opcion=0,i=0,j,x=0,aux=0,y=0,a=0,cant;
    char *h,w,z[50];
    FILE *archivo;
    while(opcion!=5)
    {
        if(x==0)
        {
            while(opcion!=1 && opcion!=4 )
            {
                cout <<endl << "\t" << "***Menu del programa***"<< endl;
                cout << "1. Captura alumno"<< endl;
                cout << "2. Recupera archivo"<< endl;
                cout << "3. Salir"<< endl;
                cout << "Elige una opcion: ";
                cin >> opcion;
                switch(opcion)
                {
                    case 2:
                        opcion = 4;
                    break;
                    case 3:
                        exit(1);
                    break; 
                }
            }
        }else{
            cout << endl << "\t"<< "***Menu del programa***"<< endl;
            cout << "1. Captura alumno"<< endl;
            cout << "2. Muestra capturas"<< endl;
            cout << "3. Guarda archivo"<< endl;
            cout << "4. Recupera archivo"<< endl;
            cout << "5. Salir"<< endl;
            cout << "Elige una opcion: ";
            cin >> opcion;
        }
        switch(opcion)
        {
            case 1: 
            if(i<10)
            {
                cout << "Nombre del alumno: ";
                fflush(stdin);
                cin.getline(alumno[i].nombre,50);
                cout << "Boleta del alumno: ";
                cin >> alumno[i].boleta;
                cout << "Promedio del alumno: ";
                cin >> alumno[i].promedio;
                i++;
            }else
                cout<< "No caben mas alumnos" << endl;
            break;
            case 2:
                cout << "   Nombre            Boleta         promedio" << endl;
                for(j=0;j<i;j++)
                {
                    cout << alumno[j].nombre << "          ";
                    cout << alumno[j].boleta << "             ";
                    cout << alumno[j].promedio;
                    cout << endl;
                }
            break;
            case 3:
            archivo = fopen("Datos.csv","w");
                for(j=0;j<i;j++)
                {
                    fputs(alumno[j].nombre,archivo);
                    fputs(",",archivo);
                    fprintf(archivo,"%ld",alumno[j].boleta);
                    fputs(",",archivo);
                    fprintf(archivo,"%.2f",alumno[j].promedio);
                    fputs( "\n",archivo );
                }
                fclose(archivo);
                i=0;
                cout << "***Se guardo exitosamente en el archivo***"<< endl;
            break;
            case 4:
                archivo = fopen("Datos.csv","r");
                while(1)
                {
                    w = fgetc(archivo);
                    if(w == '\n')
                    {
                        a++;
                    }
                    if(w == EOF)
                    {
                        break;
                    }
                }
                fclose(archivo);
                if(a>10)
                {
                    cout << "Son muchos alumnos a recuperar" << endl << endl;
                    break;
                }
                archivo = fopen("Datos.csv","r");
                for(j=0;j<a;j++){
                    memset(z, '\0', sizeof(z));
                    fgets(z,50,archivo);    
                    h = strtok(z,",");
                    aux=0;
                    while( h != NULL ) 
                    {
                        if(aux==0)
                        {
                            strcpy(alumno[j].nombre,h);
                        }
                        else if(aux==1)
                        {
                            alumno[j].boleta =atol(h); 
                        }
                        else if(aux==2)
                        {
                            alumno[j].promedio=atof(h);
                        }
                        h = strtok(NULL, ",");
                        aux++;
                    }
                    i++;
                }
                fclose(archivo);
                cout << endl << "****Se ha recuperado el archivo****" << endl;
            break;
            case 5: 
                exit(1);
            break;
        }
        x++;
    }
    return 0;
}