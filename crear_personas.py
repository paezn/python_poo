from Persona import Persona

juan = Persona("Juan", "Castellanos", 15)
juan.mostrarPersona()

leidy = Persona("Leidy","Alvarez", 18)
leidy.mostrarPersona()

leidy.apellidos = "Perez"
leidy.mostrarPersona()

juan = leidy

juan.mostrarPersona()