cant_hombres= int(input("Ingrese la cantidad de hombres en el aula de clase: "))
cant_mujeres= int(input("Ingrese la cantidad de mujeres en el aula de clase: "))

total_est=cant_hombres + cant_mujeres
porcent_hombres=(cant_hombres*100)/total_est
porcent_mujeres=(cant_mujeres*100)/total_est

print(f"El porcentaje representado por la cantidad de hombres en el aula de clase es de: {porcent_hombres:.2f}%")
print(f"El porcentaje representado por la cantidad de mujeres en el aula de clase es de: {porcent_mujeres:.2f}%")
