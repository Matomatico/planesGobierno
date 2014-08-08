#!/usr/bin/python
# -*- coding: utf-8 -*-
v = [
{"u" : "070000", "o" : "153" , "t" : "s", "n" : 0 , "c" : "1.Mejorar la capacidad resolutiva integral de la oferta en los establecimientos de salud con criterio de riesgo, genero, interculturalidad y etapa de vida. (C.C y Nativas y fronteras Ayacucho Vraem y Ucayali, 2 Mejoramiento de la Nutricion y seguridad Alimentaria de los ninos y ninas"},
{"u" : "070000", "o" : "153" , "t" : "s", "n" : 0 , "c" : "1.Promover programas para Incrementar el acceso a la educacion inicial.2.Mejorar la calidad educativa, dando mayor enfasis en las areas rurales, con enfoque bilingüe intercultural.3.Gestionar oportunamente al Gobierno Central el incremento de presupuesto para la docencia en los niveles mencionados."},
{"u" : "070000", "o" : "153" , "t" : "s", "n" : 0 , "c" : "1.Promover y desarrollar capacidades necesarias para la sostenibilidad y la autogestion de los servicios de saneamiento basico a nivel comunitario. 2.Mejorar y ampliar la cobertura de los servicios de saneamiento basico mediante tecnologias eficientes de tratamiento de aguas residuales y RRSS"},
{"u" : "070000", "o" : "153" , "t" : "m", "n" : 0 , "c" : "Establecimientos de salud Bien equipados principalmente en zonas vulnerables."},
{"u" : "070000", "o" : "153" , "t" : "m", "n" : 0 , "c" : "Elevar el numero de Ninos (as) con acceso a la educacion inicial, brindar estimulos en cada provincia a los mejores docentes."},
{"u" : "070000", "o" : "153" , "t" : "m", "n" : 0 , "c" : "Brindar un 100% de Cobertura a nivel Regional de Asistencia tecnica y soporte tecnico a las provincias y distritos en el tema de saneamiento basico en poblaciones vulnerables."},

{"u" : "070000", "o" : "153" , "t" : "s", "n" : 1 , "c" : "1.Promover e institucionalizar la investigacion cientifica y tecnologica con instituciones aliadas de la produccion agropecuaria.2.Promover la asociatividad de Productores Agropecuarios con enfoque de Cadenas Productivas, exportacion y abastecimiento de los mercados local y nacional de manera sosten"},
{"u" : "070000", "o" : "153" , "t" : "s", "n" : 1 , "c" : "1.Inventario, catalogacion y publicacion del patrimonio cultural, natural y la Cultura Viva e Inmaterial del Destino Cusco.2. Mejorar la oferta de servicios turisticos en la region Cusco,3Elaboracion y ejecucion de proyectos en comunidades rurales y nativas relacionadas con elturismoruralcomunitario"},
{"u" : "070000", "o" : "153" , "t" : "s", "n" : 1 , "c" : "1.Fomentar la formacion de centros de innovacion tecnologica (CITES)2.Promover mediante la participacion de los gobiernos locales e Instituciones Publicas la creacion de clusters industriales en las sub regiones con orientacion exportadora"},
{"u" : "070000", "o" : "153" , "t" : "m", "n" : 1 , "c" : "Un 100% de instituciones aliadas al gobierno regional identificadas con el crecimiento agropecuario, un 100 % de proyectos con regionales productivos con enfoque en la Zoonificacion Ecologica y Economica."},
{"u" : "070000", "o" : "153" , "t" : "m", "n" : 1 , "c" : "Cada provincia de nuestra region se Fortalecera a sus principales fiestas de parte del Gobierno Regional. Articulando con los principales circuitos turisticos de la region."},
{"u" : "070000", "o" : "153" , "t" : "m", "n" : 1 , "c" : "Creacion de CITEs en 3 cadenas productivas identificadas de relevancia en la region cusco"},

{"u" : "070000", "o" : "153" , "t" : "s", "n" : 2 , "c" : "1.Construccion de sistemas de riegos tecnificado por cuencas para dar un uso adecuado de recurso hidrico.2.Promover y concertar la conservacion de las cuencas hidrograficas con mejores potencialidades de la actividad agropecuaria.3.Fomentar el uso legalizado del recurso hidrico en convenio(ALA,ANA)"},
{"u" : "070000", "o" : "153" , "t" : "s", "n" : 2 , "c" : "1.Planeamiento y ordenamiento Territorial para el desarrollo urbano y sostenido, que permita el saneamiento urbano regional y asi mismo promover la cobertura y calidad habitacional Programa regional.2.Promover la Z.E.E y O.T. en gobiernos locales,Implementar estrategias para el monitoreo ambiental"},
{"u" : "070000", "o" : "153" , "t" : "s", "n" : 2 , "c" : "1.Desarrollar y actualizar el Plan Vial que permita organizar, dirigir y ejecutar las actividades de Construccion, Mejoramiento, Rehabilitacion y Mantenimiento de carreteras y puentes.2.Impulsar a la empresa privada en la cobertura de servicios de telecomunicaciones a centros alejados."},
{"u" : "070000", "o" : "153" , "t" : "m", "n" : 2 , "c" : "Un 100 % de comunidades concientes del uso sostenible de nuestros recursos hidricos capacitados legalizados."},
{"u" : "070000", "o" : "153" , "t" : "m", "n" : 2 , "c" : "Implementar en 3 de las mas grande urbes de la region centros de monitoreo ambiental y de fiscalizacion."},
{"u" : "070000", "o" : "153" , "t" : "m", "n" : 2 , "c" : "Actualizar el Plan Vial de la Region Cusco, e implementarlo en un 50% de sus actividades con fondos propios y bajo convenio."},

{"u" : "070000", "o" : "153" , "t" : "s", "n" : 3 , "c" : "1. Institucionalizacion del Consejo de Desarrollo Regional, 2. Incrementar la capacidad operativa de los organos de control interno institucionales.3. Actualizacion y Evaluacion periodica del Servidor Publico del Gobierno Regional"},
{"u" : "070000", "o" : "153" , "t" : "s", "n" : 3 , "c" : "1.Mejorar la implementacion, equipamiento y capacitacion del area de serenazgo municipal en convenio con Gobiernos Locales. 2.Implementacion y capacitacion al area de defensa civil del Gob. Regional 3.Identificar zonas de riesgo y vulnerables para promover la seguridad social ante desastres naturale"},
{"u" : "070000", "o" : "153" , "t" : "m", "n" : 3 , "c" : "El Organo de Control Institucional regional Implementado Logisticamente y con especialistas funcionarios provos."},
{"u" : "070000", "o" : "153" , "t" : "m", "n" : 3 , "c" : "Seguridad Ciudadana fortalecida e implementada en la region del cusco; realizar convenios con los gobiernso locales sobre gestion de riesgos con el 100% de provincias en el tenor de capacitacion y asistencia tecnica."},


{"u" : "070000", "o" : "601" , "t" : "s", "n" : 0 , "c" : "Objetivo Estrategico: Mejorar la Calidad Educativa Regional: Reestructuracion curricular Regional ; Capacitacion de los docentes; Construccion, rehabilitacion y equipamiento con TICS de las instituciones educativas; articulacion de la educacion basicraa, tecnica superior y universitaria"},
{"u" : "070000", "o" : "601" , "t" : "s", "n" : 0 , "c" : "Objetivo Estrategico: Reducir los indices de desnutricion infantil y mortalidad materno infantil; asi como asegurar el acceso de la poblacion, principalmente del ambito rural, a los servicios de salud, impulsando desde la Region la cobertura de 100% de atencion de atencion en salud y vivienda"},
{"u" : "070000", "o" : "601" , "t" : "s", "n" : 0 , "c" : "se tiene considerado para bajar los niveles de pobreza en nuestra region potenciaremos la articulacion de los corredores economicos, integrado a los corredores turisticos con un buen mantenimiento permanente de las vias de comunicacion, de carreteras, ferroviarias, como se describe en el cuadro N°"},
{"u" : "070000", "o" : "601" , "t" : "m", "n" : 0 , "c" : "lograr al 100% de las propuestas alcanzadas del plan regional"},
{"u" : "070000", "o" : "601" , "t" : "m", "n" : 0 , "c" : "lograr al 100% de las propuestas alcanzadas del plan regional"},
{"u" : "070000", "o" : "601" , "t" : "m", "n" : 0 , "c" : "lograr al 100% de las propuestas alcanzadas del plan regional"},

{"u" : "070000", "o" : "601" , "t" : "s", "n" : 1 , "c" : "Objetivo Estrategico: Concluir los servicios de energia electrica hacia los asentamientos rurales de la Region.Objetivo Estrategico: Elaborar del Plan Energetico Regional con estudios de demanda y oferta con clara definicion del horizonte temporal de beneficio interno."},
{"u" : "070000", "o" : "601" , "t" : "s", "n" : 1 , "c" : "Ampliar, mejorar y construir infraestructura vial regional implementar el sistema ferroviario y por corredores economicos, para alcanzar una optima articulacion e integracion economica al interior de la Region y con el entorno nacional e internacional. considerando el programa de puentes."},
{"u" : "070000", "o" : "601" , "t" : "s", "n" : 1 , "c" : "mejorando la calidad de los servicios turisticos, de acuerdo a los estandares de calidad nacional e internacional y promocionando nuevas alternativas turisticas.(Diversificacion de puntos de atraccion, Puesta en valor ligada a modernidad tecnologica, quebrar el enclave y Monopolio de Servicios."},
{"u" : "070000", "o" : "601" , "t" : "m", "n" : 1 , "c" : "lograr al 100% de las propuestas alcanzadas del plan regional"},
{"u" : "070000", "o" : "601" , "t" : "m", "n" : 1 , "c" : "lograr al 100% de las propuestas alcanzadas del plan regional"},
{"u" : "070000", "o" : "601" , "t" : "m", "n" : 1 , "c" : "lograr al 100% de las propuestas alcanzadas del plan regional"},

{"u" : "070000", "o" : "601" , "t" : "s", "n" : 2 , "c" : "Gestionar adecuadamente el medio ambiente, mediante la ejecucion de acciones y proyectos orientados a reducir el deterioro ambiental y preservar la biodiversidad regional y el equilibrio ecologico, de tal manera que se logren los propositos del desarrollo sostenible."},
{"u" : "070000", "o" : "601" , "t" : "s", "n" : 2 , "c" : "Proteccion de nuestros recursos naturales (Gas, Agua, Tierra, Mineria, Agropecuario, en favor de la buena convivencia). Proteger el patrimonio cultural y natural de la Region, como parte de nuestra soberania, autoestima e identidad regional. (Politica de Gobierno Regional)."},
{"u" : "070000", "o" : "601" , "t" : "s", "n" : 2 , "c" : "Gestionar contra posibles desastres naturales, ocasionados por el cambio climatico, mediante la formulacion de estudios y la ejecucion de programas de prevencion, para mitigar los efectos generados en la produccion, mantenimiento de la obra publica y salud de la poblacion."},
{"u" : "070000", "o" : "601" , "t" : "m", "n" : 2 , "c" : "lograr al 100% de las propuestas alcanzadas del plan regional"},
{"u" : "070000", "o" : "601" , "t" : "m", "n" : 2 , "c" : "lograr al 100% de las propuestas alcanzadas del plan regional"},
{"u" : "070000", "o" : "601" , "t" : "m", "n" : 2 , "c" : "lograr al 100% de las propuestas alcanzadas del plan regional"},

{"u" : "070000", "o" : "601" , "t" : "s", "n" : 3 , "c" : "Fortalecimiento de la estructura organica del gobierno regional , adoptando un modelo organizativo horizontal, de coordinacion que permita efectivizar la descentralizacion al interior de la Region e, incorpore a las Direcciones Regionales Sectoriales como a sus organos."},
{"u" : "070000", "o" : "601" , "t" : "s", "n" : 3 , "c" : "Fortalecimiento de las capacidades de gestion de las autoridades, funcionarios y profesionales del GRC, a traves de la organizacion de eventos de capacitacion y la prevalencia de criterios tecnicos antes que politicos, en la cooptacion de funcionarios, profesionales y tecnicos del GRC."},
{"u" : "070000", "o" : "601" , "t" : "s", "n" : 3 , "c" : "Consolidar los mecanismos de participacion, vigilancia y control ciudadano, a traves del fortalecimiento del Consejo de Coordinacion Regional y de las audiencias publicas, para asegurar eficiencia y transparencia en el manejo de la inversion publica."},
{"u" : "070000", "o" : "601" , "t" : "m", "n" : 3 , "c" : "lograr el 100% de las propuestas en el plan regional"},
{"u" : "070000", "o" : "601" , "t" : "m", "n" : 3 , "c" : "lograr el 100% de las propuestas en el plan regional"},
{"u" : "070000", "o" : "601" , "t" : "m", "n" : 3 , "c" : "lograr el 100% de las propuestas en el plan regional"},


{"u" : "070000", "o" : "2644" , "t" : "s", "n" : 0 , "c" : "Impulsar el mejoramiento sustantivo en la calidad educativa regional, posibilitando que la docencia se actualice profesionalmente y los estudiantes tengan acceso a becas y credito educativo."},
{"u" : "070000", "o" : "2644" , "t" : "s", "n" : 0 , "c" : "Propiciar el fortalecimiento y universalizacion de la atencion primaria de salud preventiva, mejoramiento sustantivo de los servicios de saneamiento y combate frontal a la desnutricion cronica infantil."},
{"u" : "070000", "o" : "2644" , "t" : "s", "n" : 0 , "c" : "Fortalecer el Sistema Regional de Seguridad Ciudadana y sus Comites Provinciales y Distritales y Promover el trabajo cooperativo publico-privado y multisectorial para promover una cultura de paz y seguridad preventiva."},
{"u" : "070000", "o" : "2644" , "t" : "m", "n" : 0 , "c" : "Al 2018 contar con un Proyecto Educativo Regional debidamente concertado, y un programa de mantenimiento de infraestructura educativa inicialmente al 35 %, asi como capacitacion docente a un 30 %, y con proyeccion al 100 %."},
{"u" : "070000", "o" : "2644" , "t" : "m", "n" : 0 , "c" : "Lograr el mantenimiento y equipamiento de los postas de salud, en particular en los sectores rurales y contar con la ampliacion de los servicios de saneamiento (agua-desagüe), propiciando el consumo de agua apta para el consumo humano y adecuados habitos de higiene, en comunidades saludables."},
{"u" : "070000", "o" : "2644" , "t" : "m", "n" : 0 , "c" : "Contar con una escuela Regional de Seguridad Ciudadana, como entidad especializada para la capacitacion del personal de la PNP, Serenazgos, Juntas Vecinales y Rondas Campesinas de la region."},

{"u" : "070000", "o" : "2644" , "t" : "s", "n" : 1 , "c" : "Promover la modernizacion del sector agricola, para su competitividad y mejora de la productividad regional, orientada al sector exportador."},
{"u" : "070000", "o" : "2644" , "t" : "s", "n" : 1 , "c" : "Promover el desarrollo de las Mypes a nivel regional, priorizando los sectores estrategicos de nuestra estructura productiva."},
{"u" : "070000", "o" : "2644" , "t" : "s", "n" : 1 , "c" : "Promover el turismo como potencialidad regional, impulsando su aprovechamiento racional y sostenibilidad."},
{"u" : "070000", "o" : "2644" , "t" : "m", "n" : 1 , "c" : "Contar con programas regionales de desarrollo agricola, tecnificacion y mejora de la productividad, propiciando el adecuado manejo de suelos agricolas, en un contexto de preservacion de la biodiversidad."},
{"u" : "070000", "o" : "2644" , "t" : "m", "n" : 1 , "c" : "Contar con un Plan de Desarrollo Regional de Mypes, con ejes estrategicos como asociaciones publico-privadas, implementacion de parques industriales y acceso a fuentes de financiamiento promocionales."},
{"u" : "070000", "o" : "2644" , "t" : "m", "n" : 1 , "c" : "Contar con un plan regional de desarrollo turistico, diversificando nuestra oferta, estandarizando nuestros servicios, con una adecuada calidad y competitividad de los mismos, promover nuevos destinos no tradicionales y articular su cadena productiva regional."},

{"u" : "070000", "o" : "2644" , "t" : "s", "n" : 2 , "c" : "Promover un programa de infraestructura vial regional para la integracion economico-social."},
{"u" : "070000", "o" : "2644" , "t" : "s", "n" : 2 , "c" : "Implementar el sistema regional de gestion de riesgo de desastres y su articulacion multisectorial."},
{"u" : "070000", "o" : "2644" , "t" : "s", "n" : 2 , "c" : "Gestionar adecuadamente el medio ambiente, reduciendo el deterioro ambiental y la preservacion de nuestra biodiversidad y equilibrio ecologico."},
{"u" : "070000", "o" : "2644" , "t" : "m", "n" : 2 , "c" : "Al 2018 se dispondra de una red vial interprovincial, articulada a las redes nacionales, con su mantenimiento periodico que garantice su calidad de servicio, con financiamiento regional y nacional (GRC, MTC, Provias)."},
{"u" : "070000", "o" : "2644" , "t" : "m", "n" : 2 , "c" : "Contar con un Sistema Regional de Gestion de Riesgo de Desastres, debidamente operativo, fortalecido y con compromiso multisectorial, apoyo logistico, financiero y participacion ciudadana. Adicionalmente operara un Sistema Regional de Alerta Temprana y monitorizacion de riesgos."},
{"u" : "070000", "o" : "2644" , "t" : "m", "n" : 2 , "c" : "Contar con un sistema regional ambiental multisectorial, que garantice el desarrollo sostenible regional, y la defensa del uso racional de nuestros recursos naturales."},

{"u" : "070000", "o" : "2644" , "t" : "s", "n" : 3 , "c" : "Promover la reestructuracion de las instituciones publicas para construir un buen gobierno sobre los principios de etica en la gestion publica, eficiencia y transparencia."},
{"u" : "070000", "o" : "2644" , "t" : "s", "n" : 3 , "c" : "Fortalecer e institucionalizar los espacios, mecanismos de concertacion, participacion y vigilancia ciudadana en igualdad de oportunidades para la gobernabilidad regional y local."},
{"u" : "070000", "o" : "2644" , "t" : "s", "n" : 3 , "c" : "Institucionalizar el sistema de planeamiento regional articulado a los diferentes niveles de gobierno."},
{"u" : "070000", "o" : "2644" , "t" : "m", "n" : 3 , "c" : "Contar con una gestion moderna, eficiente, tranparente, sobre todo sobre los principios de etica y el buen manejo de los recursos del Estado en beneficio de la poblacion"},
{"u" : "070000", "o" : "2644" , "t" : "m", "n" : 3 , "c" : "Tener espacios y mecanismos de concertacion, participacion y vigilancia ciudadana en igualdad de oportunidades para la gobernabilidad regional."},
{"u" : "070000", "o" : "2644" , "t" : "m", "n" : 3 , "c" : "Contar con un sistema de planeamiento regional articulado en los diferentes niveles de gobierno."},


{"u" : "070000", "o" : "602" , "t" : "s", "n" : 0 , "c" : "Destinar mayor presupuesto en proyectos de inversion publica en educacion con los componentes de infraestructura adecuada con aulas pedagogicas, aulas de innovacion, administrativas, laboratorios, areas recreativas y otros. Inversion en Programa de Capacitacion docente con incentivos economicos"},
{"u" : "070000", "o" : "602" , "t" : "s", "n" : 0 , "c" : "Campanas de prevencion contra las enfermedades del sistema respiratorio, infecciosas, parasitarias, digestivo."},
{"u" : "070000", "o" : "602" , "t" : "s", "n" : 0 , "c" : "Promover la participacion de los medios de comunicacion en la construccion de una cultura de valores y de vigilancia. y credibilidad Luchar de manera frontal contra la corrupcion en la administracion publica, promoviendo una cultura de prevencion y erradicacion de las practicas ilicitas"},
{"u" : "070000", "o" : "602" , "t" : "m", "n" : 0 , "c" : "Equipamiento e implementacion de aulas, laboratorios y otros con tecnologia de ultima generacion. Convenio con las Universidades para la obtencion de becas para los mejores estudiantes del distrito."},
{"u" : "070000", "o" : "602" , "t" : "m", "n" : 0 , "c" : "Inversion en prevencion de enfermedades y reducir las enfermedades del sistema respiratorio, infecciosas, parasitarias, digestivo."},
{"u" : "070000", "o" : "602" , "t" : "m", "n" : 0 , "c" : "Recuperar la confianza y promover la participacion de los medios de comunicacion en la construccion de una cultura de valores y de vigilancia. y credibilidad. Disminucion de la corrupcion en la administracion publica, con cultura preventiva y erradicacion de las practicas ilicitas"},

{"u" : "070000", "o" : "602" , "t" : "s", "n" : 1 , "c" : "Promocion de mecanismos y servicios financieros que garanticen la sostenibilidad de la actividad agropecuaria. Promocion de la construccion y el mantenimiento de la infraestructura productiva agropecuaria adecuada a situaciones de riesgo de desastre."},
{"u" : "070000", "o" : "602" , "t" : "s", "n" : 1 , "c" : "Promocionar y difundir atractivos culturales, historico- arqueologicos, geograficos (paisajes), productivos (agro turismo) y condiciones para la practica de deporte de aventura. Fomentar las organizaciones que se dediquen a la actividad relacionada al turismo."},
{"u" : "070000", "o" : "602" , "t" : "s", "n" : 1 , "c" : "Realizar campanas de sensibilizacion en comercio justo a los agricultores. Promover la conformacion y formalizacion de la pequena y micro empresa con servicios de desarrollo empresarial de ellas."},
{"u" : "070000", "o" : "602" , "t" : "m", "n" : 1 , "c" : "Desarrollo pecuario y asistencia tecnica para el mejoramiento de la produccion pecuaria. Promocion de actividades de mejoramiento de la crianza de animales menores"},
{"u" : "070000", "o" : "602" , "t" : "m", "n" : 1 , "c" : "Formulacion del Plan de Desarrollo y Plan Estrategico de Desarrollo Turistico del Distrito. Promocion del turismo arqueologico, geografico (paisajes), productivo (agro turismo) y condiciones para la practica de deporte de aventura."},
{"u" : "070000", "o" : "602" , "t" : "m", "n" : 1 , "c" : "Modernizacion, reordenamiento y mejoramiento de los servicios en el mercado de abastos bajo la gestion regional. Acceso de los productores a las Ferias Locales, Regionales y Nacionales."},

{"u" : "070000", "o" : "602" , "t" : "s", "n" : 2 , "c" : "Programa de integracion de las vias carrozales en toda la region. Programa vial mejoramiento y mantenimiento de trochas carrozables y caminos vecinales."},
{"u" : "070000", "o" : "602" , "t" : "s", "n" : 2 , "c" : "Promover la implementacion del plan de ordenamiento territorial actualizado. Promover un programa distrital de zonificacion economica y ecologica."},
{"u" : "070000", "o" : "602" , "t" : "s", "n" : 2 , "c" : "Promover la conservacion de la biodiversidad y el uso sostenible de los recursos naturales. Fomentar el respeto al medio ambiente y el desarrollo de una cultura de prevencion."},
{"u" : "070000", "o" : "602" , "t" : "m", "n" : 2 , "c" : "Construccion y Mejoramiento de trochas carrozables y caminos vecinales. Ampliacion y mejoramiento de medios de comunicacion en los diferentes sectores dela region."},
{"u" : "070000", "o" : "602" , "t" : "m", "n" : 2 , "c" : "Fortalecimiento de la oficina de Defensa Territorial y Saneamiento Fisico Legal del Distrital. Desarrollar Planes y Programas de Integracion, zonificacion economica y ecologica del Distrito."},
{"u" : "070000", "o" : "602" , "t" : "m", "n" : 2 , "c" : "Capacitacion y sensibilizacion en temas de medio ambiente a nivel escolar y poblacion. Forestacion y Reforestacion de Cuencas y Micro cuencas."},

{"u" : "070000", "o" : "602" , "t" : "s", "n" : 3 , "c" : "Fortalecimiento de las capacidades de las autoridades, funcionarios y trabajadores municipales en la gestion de fuentes de financiamiento de las entidades publicas y/o privadas."},
{"u" : "070000", "o" : "602" , "t" : "s", "n" : 3 , "c" : "Realizar actividades y/o eventos de caracter cultural, artistico y deportivo, mediante el cual se promueva el liderazgo y la practica de buenos valores. En los centros educativos, con la participacion conjunta de los docentes y alumnos, realizar charlas"},
{"u" : "070000", "o" : "602" , "t" : "s", "n" : 3 , "c" : "Dotar a la region de una infraestructura productiva que contribuya a elevar sus niveles de competitividad, Implementacion del Programa Regional de Desarrollo Habitacional."},
{"u" : "070000", "o" : "602" , "t" : "m", "n" : 3 , "c" : "Capacitacion a las autoridades, funcionarios y trabajadores municipales en la gestion de fuentes de financiamiento de las entidades publicas y/o privadas. Implementar politicas adecuadas para el mejoramiento de la calidad de los servicios municipales."},
{"u" : "070000", "o" : "602" , "t" : "m", "n" : 3 , "c" : "Capacitacion a las organizaciones sociales en temas de organizacion y gestion a las diversas entidades. Apoyo y fortalecimiento de las organizaciones Sociales."},
{"u" : "070000", "o" : "602" , "t" : "m", "n" : 3 , "c" : "La region Cusco posee un desarrollo urbano planificado. La region posee diferentes plantas industriales en varias de sus provincias. La ciudad del Cusco se desarrolla hacia el sur y hacia el norte, siguiendo un en Plan de Desarrollo Urbanistico Concertado."},


{"u" : "070000", "o" : "1257" , "t" : "s", "n" : 0 , "c" : "1.- Incremento de Comprension lectora del 25.5% (2013) que logra el Nivel 2 al 35. 2.- Incremento del desempeno en matematicas del 14.5% que alcanza el nivel 2 al 2013, al 28%."},
{"u" : "070000", "o" : "1257" , "t" : "s", "n" : 0 , "c" : "1.- Reducir la desnutricion Infantil en menores de 5 anos del 16.3%-Tabla de la OMS (ano 2013) 2.- Reducir la tasa de anemia de ninos y ninas entre 6 y 36 meses de edad que al 2013 se encuentra en 56% Fuente: INEI-ENDES."},
{"u" : "070000", "o" : "1257" , "t" : "s", "n" : 0 , "c" : "1.- Incrementar el acceso de la poblacion a agua potable y sistemas de eliminacion de excretas del 79.6% de hogares rurales que cuentan con Saneamiento Basico al ano 2013, en estrecha alianza estrategica con el CNC."},
{"u" : "070000", "o" : "1257" , "t" : "m", "n" : 0 , "c" : "1.- 35% al 2018 en comprension lectora que logra el Nivel 2 2.- 28% al 2018 en mejor desempeno en matematicas"},
{"u" : "070000", "o" : "1257" , "t" : "m", "n" : 0 , "c" : "1.- 8% de Desnutricion Infantil en menores de 5 anos al ano 2018. 2.- 38% de Tasa de Anemia de ninos y ninas entre 6 y 36 meses de edad al 2018"},
{"u" : "070000", "o" : "1257" , "t" : "m", "n" : 0 , "c" : "1.- Lograr el 85% de hogares rurales que cuentan con Saneamiento Basico en coordinacion con el Ministerio de Vivienda , el MINSA y el CNC."},

{"u" : "070000", "o" : "1257" , "t" : "s", "n" : 1 , "c" : "Proponer una iniciativa legislativa al Congreso de la Republica para que se apruebe el Canon Turistico a traves del Consejo Regional de Turismo."},
{"u" : "070000", "o" : "1257" , "t" : "s", "n" : 1 , "c" : "Se debe implementar una politica regional de promocion y reactivacion del sector industrial"},
{"u" : "070000", "o" : "1257" , "t" : "s", "n" : 1 , "c" : "Establecer una alianza estrategica con el MINCETUR, Ministerio de la Produccion, el Sector Privado y la Cooperacion Internacional."},
{"u" : "070000", "o" : "1257" , "t" : "m", "n" : 1 , "c" : "La implementacion del Canon Turistico para el ano 2016."},
{"u" : "070000", "o" : "1257" , "t" : "m", "n" : 1 , "c" : "Reactivar y fortalecer el sector industrial en la Region Cusco al 2018 en coordinacion con el Ministerio de la Produccion y el Consejo Nacional de Competitividad CNC."},
{"u" : "070000", "o" : "1257" , "t" : "m", "n" : 1 , "c" : "Implementar una Politica Regional de fortalecimiento y reactivacion del Sector Industrial a partir de julio del 2015, en coordinacion con el Ministerio de Industria y Turismo , el Ministerio de la Produccion y el Consejo Nacional de Competitividad."},

{"u" : "070000", "o" : "1257" , "t" : "s", "n" : 2 , "c" : "Se debe implementar el Sistema Regional de Gestion Ambiental-SRGA, de conformidad con lo dispuesto en el Art. 53º de la Ley 27867-Ley Organica de Gobiernos Regionales."},
{"u" : "070000", "o" : "1257" , "t" : "s", "n" : 2 , "c" : "Se deben implementar los Instrumentos de Gestion Ambiental-IGA."},
{"u" : "070000", "o" : "1257" , "t" : "s", "n" : 2 , "c" : "Debe concluirse los proyectos de asfaltado de las carreteras CUSCO-PARURO y CUSCO-PAUCARTAMBO, que se iniciaron todavia en el anos 2006."},
{"u" : "070000", "o" : "1257" , "t" : "m", "n" : 2 , "c" : "Constituir el SRGA en la Region Cusco en el mes de julio del 2015."},
{"u" : "070000", "o" : "1257" , "t" : "m", "n" : 2 , "c" : "Se constituiran los Instrumentos de Gestion Ambiental-IGA , a traves de la Comision de Gestion Ambiental.CAR, en el mes agosto del 2015."},
{"u" : "070000", "o" : "1257" , "t" : "m", "n" : 2 , "c" : "Se concluira los proyectos de asfaltado de las carreteras CUSCO-PARURO y CUSCO-PAUCARTAMBO, que se iniciaron todavia en el anos 2006, a diciembre 2015."},

{"u" : "070000", "o" : "1257" , "t" : "s", "n" : 3 , "c" : "Debe implementarse el Centro Estrategico del Planeamiento Regional del Cusco-Ceplar Cusco"},
{"u" : "070000", "o" : "1257" , "t" : "s", "n" : 3 , "c" : "Debe evaluarse la Estructura Organica y Funcional del Gobierno Regional del Cusco"},
{"u" : "070000", "o" : "1257" , "t" : "m", "n" : 3 , "c" : "Se implementar´el Centro Estrategico de Planeamiento Regional-CEPLAR-Cusco en julio del 2015"},
{"u" : "070000", "o" : "1257" , "t" : "m", "n" : 3 , "c" : "Se modificara la Estructura Organica y Funcional del Gobierno Regional del Cusco en junio del 2015."},


{"u" : "070000", "o" : "2164" , "t" : "s", "n" : 0 , "c" : "Programar campanas medicas de salud preventiva y curativa en la poblaciones menos atendidas Implementar servicio de tele-medicina, para, mediante la transmision de imagenes (tomografia, resonancia) especialistas procedan con la lectura y diagnostico, comunicado en tiempo real internet"},
{"u" : "070000", "o" : "2164" , "t" : "s", "n" : 0 , "c" : "Declaracion de emergencia del sector. Gestionar la recategorizacion de los Centros de Salud en la Region y con prioridad de los Hospitales de Paucartambo, Quillabamba y Yauri Creacion organica de plazas para medicos especialistas Construccion de infraestructura equipada"},
{"u" : "070000", "o" : "2164" , "t" : "s", "n" : 0 , "c" : "Creacion de los Colegios de Alternancia Regionales, integrando el tratamiento de las 5 variables en regimen de asistencia 15/15 Implementacion de los programas \"repitencia cero\" , \"tarea en el colegio\" y \"academia regional\" Diseno Curricular adaptado a las condiciones de la region"},
{"u" : "070000", "o" : "2164" , "t" : "m", "n" : 0 , "c" : "Adquisicion de un \"Hospital Rodante\" equipado con consultorios especializados, sala de operaciones, laboratorio, equipos de tomografia, equipo de resonancia, farmacia, internet. Ejecucion de 12 campanas medicas con personal especialista contratado para tal objetivo"},
{"u" : "070000", "o" : "2164" , "t" : "m", "n" : 0 , "c" : "Incrementar los servicios de atencion de salud hospitalaria y no-hospitalaria, con mayor cobertura de especialistas, capacidad quirurgica, laboratorios y farmacos. Implementacion de telemedicina en 03 ambitos de la region"},
{"u" : "070000", "o" : "2164" , "t" : "m", "n" : 0 , "c" : "Mejora sustantiva de la poblacion escolar en comprension lectora y razonamiento matematico. Construccion de 6 Colegios de Alternancia Regionales Diseno Curricular Regional para el nivel Secundario Material Didactico distribuido en centros educativos Equipamiento moderno de centros educativos."},

{"u" : "070000", "o" : "2164" , "t" : "s", "n" : 1 , "c" : "Construccion del Terminal Terrestre donde se concentraran todas las operaciones de arribo y salida de pasajeros, los servicios para vehiculos y pasajeros Construccion de una via rapida con multiples salidas/ingresos a la ciudad que permitira conectar las vias Cusco-Juliaca con Cusco-Abancay"},
{"u" : "070000", "o" : "2164" , "t" : "s", "n" : 1 , "c" : "Integracion a la red vial nacional por la carretera de Arequipa (Imata) desde Yauri y con la red nacional a la carretera central via Satipo desde puerto Esperanza en el distrito de Pichari. Mejoramiento y ampliacion de la red vial de integracion intra-regional."},
{"u" : "070000", "o" : "2164" , "t" : "s", "n" : 1 , "c" : "Diversificar la oferta turistica existente de la region mediante la consolidacion y desarrollo de nuevos circuitos/paquetes turisticos que incluyen la construccion del equipamiento necesario. Promover y coadyuvar la inversion turistica, Consolidar el desarrollo y certificar la oferta gastronomica"},
{"u" : "070000", "o" : "2164" , "t" : "m", "n" : 1 , "c" : "Construccion del \"Gran Terminal Terrestre del Sur\", Construccion 20 km de la \"Via de las Nubes del Cusco\", Construccion de 03 complejos viales de interconexion con las vias actuales Construccion de 13 Km de autopista al Aeropuerto Chinchero"},
{"u" : "070000", "o" : "2164" , "t" : "m", "n" : 1 , "c" : "Pavimentacion de las carreteras y vias Yauri-Negromayo-Imata, Huancarani-Paucartambo-Pilcopata-Atalaya, Sicuani-Marcapata, Huarocondo-Ollantaytambo-Chillcca, Yaurisque-Acomayo Tunel de la Veronica\"; \"Puente Integracion\" sobre rio Apurimac; carretera penetracion al Bajo Urubamba"},
{"u" : "070000", "o" : "2164" , "t" : "m", "n" : 1 , "c" : "Puesta en valor de: \"Choquequirao\"; \"Senor de Huari\"; \"Kcapacnam\"; \"Nacion Ccana y el Canon de Suycutambo\"; \"Bosque de Nubes\" Certificacion de:\"Restaurantes Solidarios\", involucrados en los circuitos turisticos"},

{"u" : "070000", "o" : "2164" , "t" : "s", "n" : 2 , "c" : "Promocion de nuestros productos agricolas nativos y de la culinaria derivadas de los mismos Difusion de las bondades de los productos agricolas nativos e importancia en la economia rural Certificacion de las \"Restaurantes de Solidaridad\" que empleen directamente los productos agricolas nativos."},
{"u" : "070000", "o" : "2164" , "t" : "s", "n" : 2 , "c" : "Desarrollo del Programa Integral de Monitoreo y Control Ambiental Regional Desarrollo del programa \"Bosques CO2\" en los terrenos comunales sin actual uso economico y permita la captura del carbono, por ende de la percepcion de los bonos economicos con beneficio a los participantes."},
{"u" : "070000", "o" : "2164" , "t" : "s", "n" : 2 , "c" : "Ampliacion de la frontera agricola de todo el valle del vilcanota. Desarrollo del Plan integral de Cosecha de Agua en las principales cuencas de la region. Ejecucion del proyecto \"Sabaluyoc\" con infraestructura vial y de riego en la provincia de Paucartambo. Masificacion del Riego Tecnificado"},
{"u" : "070000", "o" : "2164" , "t" : "m", "n" : 2 , "c" : "Crear la Unidad de Certificacion de las \"Restaurantes de Solidaridad\" Certificar el 50% de los restaurantes de la ciudad del Cusco, y de las ciudades del Valle Sagrado Lograr el entendimiento en los turistas y la poblacion en general de la importancia de las \"Restaurantes de Solidaridad\""},
{"u" : "070000", "o" : "2164" , "t" : "m", "n" : 2 , "c" : "Implementar centros de control y monitoreo ambiental en cada capital de provincia de la region. Plantar 100 millones de arboles en el Programa \"Bosques CO2\""},
{"u" : "070000", "o" : "2164" , "t" : "m", "n" : 2 , "c" : "Incorporacion de 100 mil hectareas a la agricultura y ganaderia Atencion adecuada a los requerimientos de recurso hidrico en la actividad agropecuaria Desarrollo de 12 proyectos de afianzamiento hidrico Mejora de la infraestructura de almacenamiento y conduccion de agua en la region"},

{"u" : "070000", "o" : "2164" , "t" : "s", "n" : 3 , "c" : "Facilitar al Consejo Regional de infraestructura, equipamiento, asesoramiento y logistica para el cumplimiento de sus funciones legislativas, de control y de fiscalizacion a las entidades publicas de los ambitos locales y regional."},
{"u" : "070000", "o" : "2164" , "t" : "s", "n" : 3 , "c" : "Programa de fortalecimiento de la capacidad operativa del Gobierno Regional y de sus proyectos especiales Promocion de la inversion privada y de asociaciones publico-privadas para el desarrollo de proyectos de interes regional"},
{"u" : "070000", "o" : "2164" , "t" : "s", "n" : 3 , "c" : "Sinceramiento de la condiciones de administracion y funcionamiento de las unidades de gestion educativa y de las redes de salud, para lo que se programara la re-ingenieria de las mismas Gestion ante el gobierno central para posibilitar la creacion de plazas organicas"},
{"u" : "070000", "o" : "2164" , "t" : "m", "n" : 3 , "c" : "Ejercicio fiscalizador del Consejo Regional del Gobierno Regional durante los cuatro anos, y de los gobiernos locales con un minimo de 50 acciones anuales de fiscalizacion. Expedicion de normas regionales para facilitar la gestion, el control y fiscalizacion. Fiscalizacion de Proyectos Especiales"},
{"u" : "070000", "o" : "2164" , "t" : "m", "n" : 3 , "c" : "Incremento de la capacidad operativa del gobierno regional y de sus proyectos especiales en el 60% . Constitucion de asociaciones publico-privadas para la ejecucion de megaproyectos regionales"},
{"u" : "070000", "o" : "2164" , "t" : "m", "n" : 3 , "c" : "Profesores,,Personal medico y para-medico de la region contratados oportunamente Proceso de Racionalizacion en todas las instituciones educativas y de salud en lo referente a los aspectos de infraestructura y personal asignado"},


{"u" : "070000", "o" : "1366" , "t" : "s", "n" : 0 , "c" : "Mejorar la prestacion de los servicios de educacion, a traves de programas de capacitacion a los docentes, el equipamiento a las instituciones educativas con herramientas modernas, asi como el fortalecimiento de los espacios de gestion educativa en cada una de las Instituciones educativas."},
{"u" : "070000", "o" : "1366" , "t" : "m", "n" : 0 , "c" : "Apoyar al 90% de la docencia a traves del programa de capacitacion en educacion, y coberturar al 2018 al 100% de las Instituciones educativas del nivel inicial , primario y secundario de gestion publica con el equipamiento con tecnologias modernas."},

{"u" : "070000", "o" : "1366" , "t" : "s", "n" : 1 , "c" : "Mejorar las condiciones de asignaciones mas eficientes de los recursos productivos y las brechas de infraestructura productiva. Fortalecer a traves de capacitaciones y los fondos concursables para las asociaciones de productores a nivel regional. Gestionar la descentralizacion efectiva de los"},
{"u" : "070000", "o" : "1366" , "t" : "m", "n" : 1 , "c" : "Implementar la incubadora regional de emprendimientos agropecuarios e industrial, la descentralizacion de los centros de germoplasma de plantas y animales. Implementacion de los fondos concursables para los emprendimientos innovadores con enfoque de exportacion y a los mercados locales.."},

{"u" : "070000", "o" : "1366" , "t" : "s", "n" : 2 , "c" : "Actualizacion de la zonificacion economica y ecologica regional. Adecuamiento regional de los espacios para el desarrollo empresarial, con la provision de los servicios necesarios en coordinacion con las Municipalidades, para el desarrollo de los emprendedores."},
{"u" : "070000", "o" : "1366" , "t" : "s", "n" : 2 , "c" : "Programa de forestacion y reforestacion regional. Programa de mitigacion ante los cambios climaticos. Programa de gestion de los recursos naturales. Programa de uso de nuevos mecanismos de transporte, y el desarrollo de otras opciones para mitigar y prevenir la contaminacion ambiental."},
{"u" : "070000", "o" : "1366" , "t" : "m", "n" : 2 , "c" : "Actualizacion del plan de desarrollo de la competitividad regional. Contribuir con la adecuacion de nuevas areas de expansion urbana, ciudades satelites."},
{"u" : "070000", "o" : "1366" , "t" : "m", "n" : 2 , "c" : "Creacion de una comision tecnica para el diseno de politicas publicas de mitigacion y adecuamiento a los cambios climaticos ambientales. Programa de mitigacion ante el friaje en las provincias altas."},

{"u" : "070000", "o" : "1366" , "t" : "s", "n" : 3 , "c" : "Construccion de indicadores de buena gestion regional, para solicitar a organismos nacionales e internacionales para el apoyo en el control del manejo de los recursos publicos regionales. Fortalecimiento de los comites de vigilancia de los programas sociales, proyectos regionales, incorporando a"},
{"u" : "070000", "o" : "1366" , "t" : "m", "n" : 3 , "c" : "Creacion de una plataforma virtual semantica, dinamica y activa para generar procesos de transparencia. Consolidar las alianzas estrategicas con los organismos internacionales, nacionales y la sociedad civil para vigilar, controlar y el cumplimiento de acuerdos de la gestion publica regional."},


{"u" : "070000", "o" : "2366" , "t" : "s", "n" : 0 , "c" : "-	Salud de calidad para todos, aplicando politicas de salud preventivas. -	Garantizar los servicios de saneamiento basico ambiental."},
{"u" : "070000", "o" : "2366" , "t" : "m", "n" : 0 , "c" : "Cambio de Actitud :Lucha frontal contra la corrupcion, transparencia, democracia participativa y descentralizada, control ciudadano;"},

{"u" : "070000", "o" : "2366" , "t" : "s", "n" : 1 , "c" : "- Propiciar la mineria sostenible y responsable. -	Promover el desarrollo de Energia Gasifera sostenible e Hidroelectricas."},
{"u" : "070000", "o" : "2366" , "t" : "m", "n" : 1 , "c" : "Implementar el desarrollo sostenible del sector minero y energetico, incentivando la inversion privada con responsabilidad ambiental y proteccion de la sociedad en su conju"},

{"u" : "070000", "o" : "2366" , "t" : "s", "n" : 2 , "c" : "Potenciar y promover la gestion de riesgos de desastre en lugares vulnerables.. Garantizar la sostenibilidad y sustentabilidad de los recursos naturales y la biodiversidad."},
{"u" : "070000", "o" : "2366" , "t" : "m", "n" : 2 , "c" : "-	Implementar politicas sostenibles de los recursos naturales, preservando la biodiversidad natural, cultural, la calidad ambiental e incorporando la cultura de gestion de riesgos. - Observar con inteligente propuesta el cambio climatico y a la reduccion del riesgo de desastres"},

{"u" : "070000", "o" : "2366" , "t" : "s", "n" : 3 , "c" : "-	Consolidar la reforma del estado y descentralizacion. -	Impulsar la modernizacion y restructuracion del estado regional. - Promover la articulacion e integracion institucional. - Promover la participacion ciudadana y democracia. - Impulsar la articulacion y fortalecimiento del sistema regional"},
{"u" : "070000", "o" : "2366" , "t" : "m", "n" : 3 , "c" : "-	Desarrollar una institucionalidad basada en valores (solidaridad, reciprocidad, la no discriminacion, transparencia), que relieve la identidad, lo ambiental, lo patrimonial y la diversidad, desde un tejido organizacional cohesionado orientado al desarrollo humano sostenible, con equidad, democraci"},


{"u" : "070000", "o" : "4" , "t" : "s", "n" : 0 , "c" : "Estructuracion y funcionamiento del Consejo Regional de Salud y la organizacion del Sistema"},
{"u" : "070000", "o" : "4" , "t" : "s", "n" : 0 , "c" : "Proyectos de educacion docente por especialidades, de caracter permanente."},
{"u" : "070000", "o" : "4" , "t" : "s", "n" : 0 , "c" : "Generar un plan de desarrollo del conocimiento cientifico y tecnologico en las areas agropecuarias e industriales."},
{"u" : "070000", "o" : "4" , "t" : "m", "n" : 0 , "c" : "Creacion del Consejo Regional de Salud con plena participacion de los beneficiarios."},
{"u" : "070000", "o" : "4" , "t" : "m", "n" : 0 , "c" : "Elevar en 70% el actual indice de competitividad regional."},
{"u" : "070000", "o" : "4" , "t" : "m", "n" : 0 , "c" : "Corto y mediano plazo."},

{"u" : "070000", "o" : "4" , "t" : "s", "n" : 1 , "c" : "Promover la elaboracion y ejecucion de planes y programas que viabilicen las empresas industriales."},
{"u" : "070000", "o" : "4" , "t" : "s", "n" : 1 , "c" : "Generacion de empleo para la poblacion rural."},
{"u" : "070000", "o" : "4" , "t" : "s", "n" : 1 , "c" : "Explotacion minera que beneficie a los grupos sociales del area de influencia."},
{"u" : "070000", "o" : "4" , "t" : "m", "n" : 1 , "c" : "Corto y mediano plazo."},
{"u" : "070000", "o" : "4" , "t" : "m", "n" : 1 , "c" : "Ejecucion de proyectos de riego tecnificado, aprovechando aguas almacenadas, principalmente en la pradera andina ubicada basicamente en Espinar, Chumbivilcas, Canas, Canchis, Quispicanchi y Paruro."},
{"u" : "070000", "o" : "4" , "t" : "m", "n" : 1 , "c" : "Proyectos de desarrollo social y de mejora de la educacion, en la provincia de Espinar y zonas mineras."},

{"u" : "070000", "o" : "4" , "t" : "s", "n" : 2 , "c" : "Identificacion de la demanda vinculada al ordenamiento territorial."},
{"u" : "070000", "o" : "4" , "t" : "s", "n" : 2 , "c" : "Elaboracion del Plan Integral de Vialidad, Transportes y Comunicaciones."},
{"u" : "070000", "o" : "4" , "t" : "s", "n" : 2 , "c" : "Elaboracion del Plan de Gestion Ambiental."},
{"u" : "070000", "o" : "4" , "t" : "m", "n" : 2 , "c" : "Elevados costos financieros y deficiente acceso al credito."},
{"u" : "070000", "o" : "4" , "t" : "m", "n" : 2 , "c" : "Mejoramiento y mantenimiento integral del sistema vial existente."},
{"u" : "070000", "o" : "4" , "t" : "m", "n" : 2 , "c" : "Logistica de operaciones de modificacion del tiempo con vehiculos aereos no tripulados UAV."},

{"u" : "070000", "o" : "4" , "t" : "s", "n" : 3 , "c" : "Cualificacion de la administracion regional modernizandola tecnica y operativamente."},
{"u" : "070000", "o" : "4" , "t" : "s", "n" : 3 , "c" : "Aplicacion de programas de capacitacion interinstitucional y poblacional."},
{"u" : "070000", "o" : "4" , "t" : "s", "n" : 3 , "c" : "Difusion de valores y concientizacion en la pagina web."},
{"u" : "070000", "o" : "4" , "t" : "m", "n" : 3 , "c" : "Meritocracia en vigencia para los concursos de ingreso de personal en las instancias regionales."},
{"u" : "070000", "o" : "4" , "t" : "m", "n" : 3 , "c" : "Elaboracion de planes y programas de seguridad publica, bajo el liderazgo del Gobierno Regional."},
{"u" : "070000", "o" : "4" , "t" : "m", "n" : 3 , "c" : "Formacion de grupos de monitoreo orientado a la mejora en seguridad."},


{"u" : "070000", "o" : "2368" , "t" : "s", "n" : 0 , "c" : "PROTECCION Y GESTION DE RIESGOS CONTRA INUNDACIONES EN 38 KM. DEL CAUCE DEL RIO HUATANAY EN LAS PROVINCIAS DE CUSCO Y QUISPICANCHI - REGION CUSCO"},
{"u" : "070000", "o" : "2368" , "t" : "s", "n" : 0 , "c" : "MEJORAMIENTO Y AMPLIACION DE SERVICIOS EDUCATIVOS DEL NIVEL INICIAL ESCOLARIZADO CICLO II DE LAS I.E.I. CREADAS LOS ANOS 2011-2012 DE LOS DISTRITOS DE LIVITACA, CHAMACA, VELILLE, CCAPACMARCA Y COLQUEMARCA DE LA PROVINCIA DE CHUMBIVILCAS - CUSCO"},
{"u" : "070000", "o" : "2368" , "t" : "s", "n" : 0 , "c" : "AMPLIACION DE SERVICIOS EDUCATIVOS DEL NIVEL INICIAL ESCOLARIZADO CICLO II DE LAS I.E.I. CREADAS EN EL ANO 2012 DE LOS DISTRITOS DE SANTO TOMAS, LLUSCO Y QUINOTA DE LA PROVINCIA DE CHUMBIVILCAS - CUSCO"},
{"u" : "070000", "o" : "2368" , "t" : "m", "n" : 0 , "c" : "533,585 Habitantes beneficiados en las provincias de Cusco y Quispicanchi, el area de intervencion esta constituida por los distrito de: Santiago, Wanchaq, San Sebastian, San Jeronimo, Saylla, Oropesa y Lucre."},
{"u" : "070000", "o" : "2368" , "t" : "m", "n" : 0 , "c" : "4,535 ninos Beneficiarios de 3 a 5 anos de la provincia de Chumbivilcas – Region Cusco."},
{"u" : "070000", "o" : "2368" , "t" : "m", "n" : 0 , "c" : "5,143 ninos beneficiarios de 3 a 5 anos en los distritos de Livitaca, Chamaca, Velille, Ccapacmarca y Colquemarca de la provincia de Chumbivilcas, poblaciones es rural."},

{"u" : "070000", "o" : "2368" , "t" : "s", "n" : 1 , "c" : "VIA EXPRESA DE LA CIUDAD DEL CUSCO: OVALO LOS LIBERTADORES - PUENTE COSTANERA - NODO DE VERSALLES"},
{"u" : "070000", "o" : "2368" , "t" : "s", "n" : 1 , "c" : "MEJORAMIENTO DE LA TRANSITABILIDAD PEATONAL Y VEHICULAR DE LA AVENIDA EVITAMIENTO DE LA CIUDAD DEL CUSCO"},
{"u" : "070000", "o" : "2368" , "t" : "s", "n" : 1 , "c" : "CARRETERA: RANRACASSA - COLQUEMARCA - DV. VELILLE - CHAMACA - TUNGASUCA - YANAOCA - YAURI; VARIANTE DV. TUNGASUCA - INTEGRACION KANA (QUIRIPAMPA); ACCESO SANTO TOMAS - DV. VELILLE Y ACCESO VELILLE - DV. SANTO TOMAS."},
{"u" : "070000", "o" : "2368" , "t" : "m", "n" : 1 , "c" : "165,533 beneficiarios pobladores de la zona urbana de los principales distritos de la provincia de Cusco, dedicados basicamente a actividades de servicio y comercio, los que tienen dificultades para movilizarse, debido a que la via expresa se encuentra en mal estado."},
{"u" : "070000", "o" : "2368" , "t" : "m", "n" : 1 , "c" : "410,963 habitantes beneficiarios. Con una tasa de crecimiento promedio de 3.92%.las principales actividades economicas son el sector comercio, servicios y turismo."},
{"u" : "070000", "o" : "2368" , "t" : "m", "n" : 1 , "c" : "106,273 beneficiarios la poblacion beneficiada se dedica en su mayoria a la produccion agricola y ganadera en las localidades de Yauri, Paruro, Livitaca, Colquemarca, Yanaoca entre otros."},

{"u" : "070000", "o" : "2368" , "t" : "s", "n" : 2 , "c" : "MEJORAMIENTO DE LA DEMARCACION TERRITORIAL DEL AMBITO REGIONAL CUSCO"},
{"u" : "070000", "o" : "2368" , "t" : "s", "n" : 2 , "c" : "MEJORAMIENTO DEL SISTEMA DE LA GESTION INTEGRAL DE LOS RESIDUOS SOLIDOS EN LOS DISTRITOS DE URUBAMBA, CHINCHERO, HUAYLLABAMBA, MARAS, OLLANTAYTAMBO, YUCAY Y DISPOSICION FINAL PARA EL DISTRITO DE MACHUPICCHU, PROVINCIA DE URUBAMBA, REGION CUSCO"},
{"u" : "070000", "o" : "2368" , "t" : "s", "n" : 2 , "c" : "MEJORAMIENTO Y CONSOLIDACION DE LA GESTION INTEGRADA DE LOS RECURSOS HIDRICOS EN LA CUENCA DEL VILCANOTA - URUBAMBA DE LA REGION CUSCO"},
{"u" : "070000", "o" : "2368" , "t" : "m", "n" : 2 , "c" : "1’315,853 De Beneficiarios poblacion de la region del Cusco."},
{"u" : "070000", "o" : "2368" , "t" : "m", "n" : 2 , "c" : "34,368 habitantes de la zona urbana de la provincia de Urubamba, Chinchero, Huayllabamba, Machupicchu, Maras, Ollantaytambo y Yucay. La poblacion total de la provincia de Urubamba"},
{"u" : "070000", "o" : "2368" , "t" : "m", "n" : 2 , "c" : "960,736 beneficiarios de las provincias Acomayo, Quispicanchi, Cusco, La Convencion, Canchis Canas, Urubamba, Paucartambo, Anta Acomayo, Calca"},

{"u" : "070000", "o" : "2368" , "t" : "s", "n" : 3 , "c" : "GESTION PUBLICA EFICIENTE, EFICAZ Y TRANSPARAENTE CON VALORES QUE PROMUEVAN EL DESARROLLO REGIONAL"},
{"u" : "070000", "o" : "2368" , "t" : "s", "n" : 3 , "c" : "MEJORAR LA SEGURIDAD CIUDADANA EN COORDINACION CON LA POLICIA NACIONAL"},
{"u" : "070000", "o" : "2368" , "t" : "m", "n" : 3 , "c" : "50% de los servidores publicos acreditados"},
{"u" : "070000", "o" : "2368" , "t" : "m", "n" : 3 , "c" : "Reducir la delincuencia en la Provincia de Cusco"},


{"u" : "070000", "o" : "5" , "t" : "s", "n" : 0 , "c" : "-Ampliar la cobertura de los servicios de salud en la region -Construccion del centro de atencion Materno perinatal en la region. -Construccion del Hospital del nino en el Cusco. -Promover la salud preventiva y promocional dirigida a la gestante, madre y el neonato."},
{"u" : "070000", "o" : "5" , "t" : "s", "n" : 0 , "c" : "-	Ampliar las oportunidades y la calidad de la atencion integral en educacion. -	Revolucion tecnologica educativa regional -	Fortalecimiento de capacidades a los docentes y directivos para la convivencia sin violencia en instituciones educativas -	crear un espacio educativo especializado para person"},
{"u" : "070000", "o" : "5" , "t" : "s", "n" : 0 , "c" : "-	implementar un programa de saneamiento basico regional -	Creacion del centro de atencion especializado de la mujer en situacion de violencia a nivel de toda la region. -	Fomentar la implementacion de centros recreacionales deportivos y de alto rendimiento en la region de Cusco,"},
{"u" : "070000", "o" : "5" , "t" : "m", "n" : 0 , "c" : "-Al 2018 hemos reducido la mortalidad materno perinatal en 90% -Al 2018 la cobertura de atencion del poblador cusqueno se ha incrementado en un 90% -Al 2018 el 95% de ninos menores de 5 anos se han realizado el control para reducir la desnutricion."},
{"u" : "070000", "o" : "5" , "t" : "m", "n" : 0 , "c" : "-	Al 2018 el 95% de ninos y jovenes en edad escolar se encuentran en sus aulas recibiendo clases - Cobertura en un 80% de instituciones educativas - Reduccion del fenomeno de violencia en escuelas. - Articular rutas de aprendizaje para que los alumnos integren a cualquier institucion educativa."},
{"u" : "070000", "o" : "5" , "t" : "m", "n" : 0 , "c" : "-	Al 2018 se ha coberturado el 90% de saneamiento basico en la region -	Al 2018 los indices de delincuencia han disminuido en un 90%. -	Al 2018 contar con 4 centros recreacionales deportivos y de alto rendimiento (Chumbivilcas, Urubamba, Cusco y La Convencion)."},

{"u" : "070000", "o" : "5" , "t" : "s", "n" : 1 , "c" : "-	Implementar un programas para mejorar la produccion agropecuaria “PROGRAMA HATUNRUNA AGRICULTOR” -	Promover la creacion y formalizacion de las micro y pequenas empresas informales, mejorando su capacidad de gestion, acceso al credito, asistencia tecnica y capacitacion asi como la organizacion de p"},
{"u" : "070000", "o" : "5" , "t" : "s", "n" : 1 , "c" : "-	Fortalecer las Instituciones publicas y privadas eficientes y modernas para promover el Desarrollo Economico Regional (creacion de parques industriales, Centros de Investigacion y Transferencia Tecnologica en cada provincia)."},
{"u" : "070000", "o" : "5" , "t" : "s", "n" : 1 , "c" : "-	Promocion de circuitos turisticos para revalorar el patrimonio cultural y natural, incentivando el turismo local, nacional e internacional PROGRAMA HATUNQOSQO”"},
{"u" : "070000", "o" : "5" , "t" : "m", "n" : 1 , "c" : "-	Al 2018 el 50% de pobladores dedicados a la produccion agropecuaria han mejorado su trabajo y se han enlazado a la cadena de mercado de productos. -	Al 2018 el 80% de las micro y pequenas esten formalizadas."},
{"u" : "070000", "o" : "5" , "t" : "m", "n" : 1 , "c" : "-	Al 2018 la region de cusco contara con 4 parques industriales en las provincias de (Cusco, Canchis, Calca y la convencion)."},
{"u" : "070000", "o" : "5" , "t" : "m", "n" : 1 , "c" : "-	Al 2018 el 60% del patrimonio cultural y natural se han puesto en valor -	Mejorar el acceso de accesos a todos los circuitos turisticos. -	Al 2018 el 80% de las areas naturales protegidas del cusco y las areas de conservacion regional se han implementado para la proteccion y promocion de la activi"},

{"u" : "070000", "o" : "5" , "t" : "s", "n" : 2 , "c" : "-	Implementacion del proyecto de terminales terrestres en la zona norte y sur del Cusco. -	Elaboracion y ejecucion del plan Vial Regional, -Articulacion de las vias a nivel de toda la region. -Elaboracion y ejecucion del proyecto del tunel de la Veronica."},
{"u" : "070000", "o" : "5" , "t" : "s", "n" : 2 , "c" : "-Implementar 3 viveros forestales tecnificados en la zona andina, altoandina y amazonica para la produccion de 6 millones de plantones anuales. -Creacion de la Autoridad Ambiental Regional ARA cusco."},
{"u" : "070000", "o" : "5" , "t" : "s", "n" : 2 , "c" : "-Elaborar y ejecutar un proyecto de educacion ambiental regional para la recuperacion de nuestra cultura ambiental como la de nuestros ancestros los INCAS “PROGRAMA HATUNRUNA ECOLOGISTA”"},
{"u" : "070000", "o" : "5" , "t" : "m", "n" : 2 , "c" : "-Al 2018 funcionan adecuadamente los dos terminales terrestres en la zona norte y sur del Cusco -Al 2018 el 80% de las vias de la region Cusco estan terminadas y en circulacion."},
{"u" : "070000", "o" : "5" , "t" : "m", "n" : 2 , "c" : "-	Al 2018 incrementar el 50% de plantones en los viveros tecnificados para incrementar la cobertura vegetal en la Region. -Al 2018 el 100% de las actividades productivas y extractivas son supervisadas y evaluadas para no generar impactos negativos en el ambiente."},
{"u" : "070000", "o" : "5" , "t" : "m", "n" : 2 , "c" : "-	Al 2015 se ha implementado el proyecto de educacion ambiental -Al 2018 el 100% de instituciones educativas de la Region del Cusco han implementado la politica Regional de educacion ambiental"},

{"u" : "070000", "o" : "5" , "t" : "s", "n" : 3 , "c" : "-Implementar sub regiones del gobierno regional que tenga autonomia administrativa y tecnica, que permita el desarrollo sub regional y promueva la economia local."},
{"u" : "070000", "o" : "5" , "t" : "s", "n" : 3 , "c" : "-Lograr la integracion politica territorial que vaya conformando unidades territoriales dirigidas hacia la consolidacion de la Macro region Sur para lograr una real autonomia en el proceso de descentralizacion de funciones regionales."},
{"u" : "070000", "o" : "5" , "t" : "s", "n" : 3 , "c" : "-Fortalecimiento de los sistemas de control, supervision, fiscalizacion y vigilancia ciudadana, con profesionales especializados en administracion publica."},
{"u" : "070000", "o" : "5" , "t" : "m", "n" : 3 , "c" : "-Para el ano 2016 tener implementado las sub regiones en su totalidad, a nivel de toda la region."},
{"u" : "070000", "o" : "5" , "t" : "m", "n" : 3 , "c" : "-Al 2018 en un 90% se han implemtando politicas de articulacion regional logrando integracion a nivel distrital y provincial."},
{"u" : "070000", "o" : "5" , "t" : "m", "n" : 3 , "c" : "-Gestion transparente y libre de corrupcion."},


{"u" : "070000", "o" : "1555" , "t" : "s", "n" : 0 , "c" : "Implementar los Comites de Gestion “QALIWAWA Implementar el Programa de Seguridad Alimentaria Regional - PROSAR"},
{"u" : "070000", "o" : "1555" , "t" : "s", "n" : 0 , "c" : "Recategorizacion y adecuada capacidad resolutiva de EE.SS. a nivel regional Fortalecer niveles hospitalarios I y II con infraestructura y equipamiento al 100% Equipar Casas Maternas en todos los establecimientos de Salud Mejoramiento facultades de medicina Especializar profesionales en Salud"},
{"u" : "070000", "o" : "1555" , "t" : "s", "n" : 0 , "c" : "Centro Altos Estudios Regionales Promocion de la Investigacion Prog Educacion Integral AMAUTA Creditos a Estudiantes Universitarios, Autoevaluacion docente. Sistemas educacion alternativa Fondo Rotatorio de vivienda Programa QHALIWASI Plantas de Tratamiento en provincias"},
{"u" : "070000", "o" : "1555" , "t" : "m", "n" : 0 , "c" : "Implementacion de 108 Comites locales de QALIWAWA Reduccion de la desnutricion cronica al 20% a nivel regional"},
{"u" : "070000", "o" : "1555" , "t" : "m", "n" : 0 , "c" : "Funcionamiento adecuado de los Hospitales en todas las provincias de la region, Infraestructura mejorada y equipada al 100% en el 2018 108 distritos con Casas Maternas equipadas adecuadamente Convenio con Universidades UNSAAC y UAC Un minimo de 400 profesionales de la salud capacitados"},
{"u" : "070000", "o" : "1555" , "t" : "m", "n" : 0 , "c" : "Fondo Rotatorio COFOPRI descentralizado Ordenanza de proteccion de seguridad hidrica de fuentes de agua para consumo humano Transferencia de DIGESA Convenios para mejorar los Servicios Municipales de Residuos Solidos Convenio con Universidades para investigacion 100 jovenes ano con becas"},

{"u" : "070000", "o" : "1555" , "t" : "s", "n" : 1 , "c" : "Fomentar MyPEs juveniles Centro Innovacion tecnologica. Mejorar puertos comerciales Urcos, Sicuani, Espinar, Anta Priorizar adquisiciones a proveedores cusquenos Parque Industrial Cusco y Cachimayo Incentivos adquisicion vehiculos nuevos Tunel Av. Ejercito Poroy Aerodromos"},
{"u" : "070000", "o" : "1555" , "t" : "s", "n" : 1 , "c" : "Reconversion productiva agraria Cosecha de agua regional Mecanizacion Agricola Industrializar productos andinos. Patentes recursos geneticos andinos Planificacion Productiva Fortalecer asociatividad Servicios financieros agropecuarias Revaloracion actividades historicos y modernos"},
{"u" : "070000", "o" : "1555" , "t" : "s", "n" : 1 , "c" : "Pavimentacion Ejes Viales por Corredores Economicos en con Gobiernos Locales Promocion turismo comunitario Recuperar destino Choquequiraw Promover turismo local en corredores gastronomicos Valle Sur, Sagrado, Pampa de Anta Proteger herencia cultural, natural e identidad andina y amazonica"},
{"u" : "070000", "o" : "1555" , "t" : "m", "n" : 1 , "c" : "Convenio con SUNAT, MINTRA, MUNICIPALIDADES Registro Unico de Mypes Centro de Innovacion tecnologica regional Mejoramiento de 02 parques industriales Contrato de ejecucion de tunel Av. Ejercito – Poroy Estudios de factibilidad de mejoramiento de aerodromos y de sistemas multimodales en la region"},
{"u" : "070000", "o" : "1555" , "t" : "m", "n" : 1 , "c" : "01 Proyecto Mecanizacion Agricola AYNI nivel comunal por vocacion agricola Proyecto industrializacion productos agricolas andinos. Registro de Patentes Plan Desarrollo Agrario Regional Proyecto Fortalecimiento asociatividad Convenios con entidades financieras Ordenanza de proteccion"},
{"u" : "070000", "o" : "1555" , "t" : "m", "n" : 1 , "c" : "Asfaltado de vias por corredores economicos Infraestructura de Integracion Regional Cusco – Apurimac. Infraestructura Vial de acceso a Machupicchu. Asfaltados de vias de corredores turisticos a nivel regional Ordenanza Regional de promocion de tarifas reducidas de turismo para los cusquenos"},

{"u" : "070000", "o" : "1555" , "t" : "s", "n" : 2 , "c" : "Tratos justos sobre Recursos Hidricos con Gob. Nac y Empresas Negociar con concesionarias y Gob. Nac. precio del gas Regionalizar explotacion Gas de Camisea Inversion minera con responsabilidad social y ambiental Fondo socio-ambiental con empresas mineras, EIA en proyectos Regionales"},
{"u" : "070000", "o" : "1555" , "t" : "s", "n" : 2 , "c" : "Programa de Seguridad Hidrica de proteccion de fuentes de agua para consumo humano Promover la agricultura organica y establecer mecanismos para su certificacion. Programa de forestacion CIEN MILLONES DE ARBOLES PARA LA VIDA Campana masiva de recuperacion de cobertura vegetal, recarga acuiferos"},
{"u" : "070000", "o" : "1555" , "t" : "s", "n" : 2 , "c" : "Construir Termoelectrica de Quillabamba. Construir Hidroelectricas a nivel regional Formalizacion mineria informal Gestion integral de cuencas, Implementar la GRD. Programa Cosecha de Aguas Una comunidad, una presa Crear areas de conservacion y preservacion ambiental Prohibir cultivo de transgenico"},
{"u" : "070000", "o" : "1555" , "t" : "m", "n" : 2 , "c" : "Convenio con Empresas y Gobierno Nacional sobre precio del gas Regionalizacion del Gas de Camisea Proyecto de Ley para reorientacion del canon hidroenergetico Convenios Marco con empresas mineras para ejecutar fondos de responsabilidad social en el ambito de intervencion de las concesiones"},
{"u" : "070000", "o" : "1555" , "t" : "m", "n" : 2 , "c" : "Reconversion de la utilizacion del agua como fuente para varios usos domestico productivo con un concepto integral. Proyecto Regional de Certificacion de cultivos organicos el 2016 Proyecto de Reforestacion implementado a nivel regional"},
{"u" : "070000", "o" : "1555" , "t" : "m", "n" : 2 , "c" : "Estudios hidroenergeticos formulados Ordenanza formalizacion mineria informal Ejecucion Programa Regional Cosecha de Aguas Ordenanza Creacion Areas de conservacion y preservacion ambiental Convenio SERNANP Convenio RAMSAR Ordenanza prohibicion transgenicos Oficina apoyo produccion limpia"},

{"u" : "070000", "o" : "1555" , "t" : "s", "n" : 3 , "c" : "Defensa derechos, saberes y conocimientos ancestrales Pueblos originarios Defensa Patrimonio Cultural, identidad y diversidad Regional Asamblea Regional Todos los Pueblos y Todos los Tiempos Centros Culturales y Museos Fondo Editorial KHIPU Fondo Cultural YACHAY Atencion integral adulto mayor"},
{"u" : "070000", "o" : "1555" , "t" : "s", "n" : 3 , "c" : "Participacion de Jovenes en comites de gestion, participativos y de gestion gubernamental con mismos derechos y deberes Reingenieria administrativa del GORE Implementar el Gobierno Electronico, Politica Eficaz de ANTI-CORRUPCION Implementacion politicas de coordinacion intraregional, con GLs"},
{"u" : "070000", "o" : "1555" , "t" : "s", "n" : 3 , "c" : "Creacion del Centro de Planeamiento Regional Cusco Implementar el Plan de Ordenamiento territorial Regional. Creacion del Programa de Emergencia de Reconstruccion Creacion de la Oficina Regional de Gestion de Conflictos Creacion de un canon turistico. Presupuesto Metropolitano para Cusco"},
{"u" : "070000", "o" : "1555" , "t" : "m", "n" : 3 , "c" : "Ordenanza proteccion derechos de pueblos originarios Ordenanza proteccion de Patrimonio Regional Implementa Asamblea Regional Todos los pueblos y todos los tiempos Ejecucion Centros Culturales Ordenanza creacion del Fondo Khipu y YACHAY Centros de recreacion, del adulto mayor y discapacitados"},
{"u" : "070000", "o" : "1555" , "t" : "m", "n" : 3 , "c" : "Respetar el cumplimiento de la Ley de Presupuesto Participativo Adecuacion de la Estructura Organizacional del GORE Ejecucion Proyecto Gobierno Electronico Ordenanza Sistemas de vigilancia ciudadana electronica y del control social Constituir Comites de Gestion de inversiones del GORE"},
{"u" : "070000", "o" : "1555" , "t" : "m", "n" : 3 , "c" : "Evaluacion, Actualizacion y alineamiento de planes comunales, distritales y provinciales al PDCRl y al Plan Bicentenario Ejecutar el Proyecto de Ordenamiento Territorial regional Convenio con Gobierno Nacional para la creacion del fondo de reconstruccion Oficina Regional de gestion de conflictos"},


{"u" : "070000", "o" : "445" , "t" : "s", "n" : 0 , "c" : "- Aplicar un curriculo educativo regional con pertinencia a la diversidad socio cultural - Establecer estandares de evaluacion de aprendizaje en los niveles educativos. - Incrementar el presupuesto para asegurar la calidad educativa"},
{"u" : "070000", "o" : "445" , "t" : "s", "n" : 0 , "c" : "- Fortalecer la DIRESA, REDES y establecimientos de salud con equipos y personal especializado; - Implementar estrategias de crecimiento y desarrollo integral de la primera infancia; - Ampliar el acceso a servicios de saneamiento basico."},
{"u" : "070000", "o" : "445" , "t" : "s", "n" : 0 , "c" : "- Fortalecer los Consejos Regionales de Juventud COREJU, de Mujer COREMU y personas con discapacidad COREDIS como espacios legitimos; -	Generar oportunidades educativas, seguro de salud y de acceso a empleo digno. - Fortalecer la participacion de jovenes, mujeres y de personas con discapacidad."},
{"u" : "070000", "o" : "445" , "t" : "m", "n" : 0 , "c" : "- 50% y 25% de nivel satisfactorio en comprension lectora y matematica. -	Monitoreo del Diseno Curricular por DREC, COPARE y Sindicatos. - 100% de II EE construidas tendran equipamiento e infraestructura moderna."},
{"u" : "070000", "o" : "445" , "t" : "m", "n" : 0 , "c" : "- 100% de establecimientos de salud equipados y profesionales; - Reducir la desnutricion cronica en menores de 05 anos a 12% y la mortalidad materno y neonatal a 50%; - Cobertura de agua y desagüe al 90% de viviendas en la region."},
{"u" : "070000", "o" : "445" , "t" : "m", "n" : 0 , "c" : "- 02 audiencias anuales del Ejecutivo Regional y el Consejo Regional con COREJU, COREMU y COREDIS; - Asignacion de presupuesto para proyectos priorizados; - 75% de jovenes, mujeres y personas con discapacidad con seguro y sistema de pensiones; - Ampliar la cuota de participacion."},

{"u" : "070000", "o" : "445" , "t" : "s", "n" : 1 , "c" : "- Promover un liderazgo regional de la DRAC; - Fortalecer la investigacion, innovacion y transferencia tecnologica en principales cultivos y crianzas. - Fortalecer la pequena agricultura familiar regional replicando las experiencias del Corredor Economico Cusco– Puno, ONGs y del sector publico."},
{"u" : "070000", "o" : "445" , "t" : "s", "n" : 1 , "c" : "- Mejorar la infraestructura vial, de interpretacion y articulacion de circuitos turisticos; - Desarrollar y promover circuitos turisticos culturales y naturales;"},
{"u" : "070000", "o" : "445" , "t" : "s", "n" : 1 , "c" : "- Formulacion participativa y concertada del Plan Estrategico de Promocion de las MYPES - Fortalecer las actividades desarrolladas por la MYPES a nivel regional. - Promover la formalizacion de la MYPES y la articulacion de su produccion al mercado internacional."},
{"u" : "070000", "o" : "445" , "t" : "m", "n" : 1 , "c" : "- 03 centros de investigacion en funcionamiento (amazonia, valle interandino y provincias altas); - Incrementar la inversion en sistemas de riego para las pequenas unidades productivas; -	Fortalecer PROCOMPITE; - 01 proyecto de inversion para el potencial pecuario de las provincias altas."},
{"u" : "070000", "o" : "445" , "t" : "m", "n" : 1 , "c" : "- Nuevos destinos turisticos articulados y con vias asfaltadas; - 03 productos turisticos desarrollados (La Convencion, Choquequirao y Provincias altas); -	01 plan de promocion de nuevos destinos turisticos (ferias, web)"},
{"u" : "070000", "o" : "445" , "t" : "m", "n" : 1 , "c" : "- 50 mil MYPES participan activamente en la ejecucion de los Proyectos en el marco del Plan Estrategico MYPE."},

{"u" : "070000", "o" : "445" , "t" : "s", "n" : 2 , "c" : "- Fortalecer la capacidad de los gobiernos, para la gestion integrada del ambiente y el ordenamiento territorial."},
{"u" : "070000", "o" : "445" , "t" : "s", "n" : 2 , "c" : "Garantizar la gestion integrada y sostenible de los recursos naturales, la conservacion de la biodiversidad natural, biocultural y la calidad ambiental para un desarrollo integral sostenible"},
{"u" : "070000", "o" : "445" , "t" : "s", "n" : 2 , "c" : "Aprovechar el potencial hidrico para la produccion de energia electrica con fines industriales y para el uso domestico."},
{"u" : "070000", "o" : "445" , "t" : "m", "n" : 2 , "c" : "- Distritos cuentan con planes de ordenamiento territorial y proteccion de areas agricolas. - Creacion de la Autoridad Ambiental Regional (AARC)"},
{"u" : "070000", "o" : "445" , "t" : "m", "n" : 2 , "c" : "- 03 mega proyectos: gestion integral del recursos hidricos; de Forestacion y Reforestacion; gestion integral de Residuos Solidos; - 01 Proyecto integrado de gestion de Riesgos de Desastres con enfoques de cambio climatico y territorial."},
{"u" : "070000", "o" : "445" , "t" : "m", "n" : 2 , "c" : "- Implantar 02 proyectos Hidroenergeticos ambientalmente sostenibles (Pane en Espinar y Salcca Pucara en Canchis); - Formular proyectos hidroenergeticos por principales cuencas de la region"},

{"u" : "070000", "o" : "445" , "t" : "s", "n" : 3 , "c" : "- Constituir una comision externa de veeduria (control y fiscalizacion) constituida por organizaciones e instituciones con credibilidad; - Fortalecer los organos de control, fiscalizacion y vigilancia (OCI, CR, CCR, Sindicato, COVIC)"},
{"u" : "070000", "o" : "445" , "t" : "s", "n" : 3 , "c" : "- Democratizar la toma de decisiones (planificacion y presupuesto participativo) - Transparentar la gestion del Gobierno Regional"},
{"u" : "070000", "o" : "445" , "t" : "s", "n" : 3 , "c" : "- Fortalecer las mancomunidades municipales; - Impulsar la integracion macro regional del sur; - Relanzar el Foro Regional del Cusco que lucho por la descentralizacion"},
{"u" : "070000", "o" : "445" , "t" : "m", "n" : 3 , "c" : "- 01 foro publico por ano de informe de la comision de veedores; - Audiencias publicas de rendicion de cuentas con intervencion de OCI, Consejo Regional, Consejo de Coordinacion Regional, Sindicato, Comite de Vigilancia Ciudadana y Ejecutivo del Gobierno Regional"},
{"u" : "070000", "o" : "445" , "t" : "m", "n" : 3 , "c" : "- Todos los proyectos pasaran por presupuesto participativo; - Consejos regionales de concertacion se reunen con Presidente, Gerentes y Consejo Regional; - Organizar audiencias de rendicion de cuentas oportunas y a detalle;"},
{"u" : "070000", "o" : "445" , "t" : "m", "n" : 3 , "c" : "- Constituir una instancia de trabajo con mancomunidades; -	Ejecutar proyectos en convenio con mancomunidades y municipalidades; - Generar debate y propuestas sobre la descentralizacion y desarrollo regional"},



{"u" : "140000", "o" : "1269" , "t" : "s", "n" : 0 , "c" : "Capacitacion docente especializada, entrega de Tablet con WIFI a los escolares, escuelas inclusivas para ninos especiales y escuela de talentos de formacion integral para secundaria. Implementacion de institutos tecnologicos, agrarios y turisticos. Mejoramiento de los mobiliarios de las I.E. y entre"},
{"u" : "140000", "o" : "1269" , "t" : "s", "n" : 0 , "c" : "Mejoramiento de la infraestructura de Hospitales y centros de salud, para atender oportunamente las enfermedades, con equipos modernos y profesionales especializados que atienden a los usuarios con calidez. Programa de apoyo nutricional focalizando la atencion al binomio madre-nino, promocion de la"},
{"u" : "140000", "o" : "1269" , "t" : "s", "n" : 0 , "c" : "Liderar la seguridad ciudadana, garantizar seguridad juridica y fortalecer las organizaciones comunales para prevenir la inseguridad ciudadana Instalacion de la Unidad de Inteligencia Financiera para que identifique y sancione el lavado de activos procedente del narcotrafico y de la corrupcion de la"},
{"u" : "140000", "o" : "1269" , "t" : "m", "n" : 0 , "c" : "Capacitacion al 100% de los docentes de la Region. Generacion de oportunidad de empleo para el 50% de los estudiantes de educacion superior. 30% de I.E con Mobiliario mejorado 50% de la Poblacion escolar con reforzamiento en comprension lectora y razonamiento logico matematico"},
{"u" : "140000", "o" : "1269" , "t" : "m", "n" : 0 , "c" : "Incremento del 70% de la cobertura de salud y reducir la desnutricion en el 80% de los sectores afectados"},
{"u" : "140000", "o" : "1269" , "t" : "m", "n" : 0 , "c" : "70% de las ciudades de la region equipadas con camara de video vigilancia, que permiten la accion inmediata de la Guardia Regional. Unidad de Inteligencia Financiera que identifica el lavado de activos y fondos procedentes de la corrupcion en el 70% de los ex - funcionarios y funcionarios de las en"},

{"u" : "140000", "o" : "1269" , "t" : "s", "n" : 1 , "c" : "Brindar apoyo al sector productivo organizado, con sistema de credito no reembolsable."},
{"u" : "140000", "o" : "1269" , "t" : "s", "n" : 1 , "c" : "Capacitar con alta tecnologia. Desarrollo de programas de cultivo. Creacion del Gran Mercado Regional para promocionar los productos de nuestra region."},
{"u" : "140000", "o" : "1269" , "t" : "s", "n" : 1 , "c" : "Politica de promocion del turismo y conservacion arqueologica. Promocion del turismo con inversion publica y privada. Programa de promocion del turismo: ferias gastronomicas. Impulso del turismo a traves de proyectos mancomunados con los gobiernos locales."},
{"u" : "140000", "o" : "1269" , "t" : "m", "n" : 1 , "c" : "Invertiremos 20 millones de soles anuales en el fondo concursable PROCOMPITE"},
{"u" : "140000", "o" : "1269" , "t" : "m", "n" : 1 , "c" : "Formacion de cadenas productivas en el 50% de las provincias de nuestra region."},
{"u" : "140000", "o" : "1269" , "t" : "m", "n" : 1 , "c" : "Incremento en un 50% de la actividad turistica regional"},

{"u" : "140000", "o" : "1269" , "t" : "s", "n" : 2 , "c" : "Dinamizar la economia regional con el impulso de la via ferroviaria de alta velocidad. Identificar los principales anillos viales orientados al desarrollo socio economico. Adoptar politicas viales y financieras por parte del Gobierno Regional."},
{"u" : "140000", "o" : "1269" , "t" : "s", "n" : 2 , "c" : "Mejoramiento de los existentes y creacion de nuevos servicios."},
{"u" : "140000", "o" : "1269" , "t" : "s", "n" : 2 , "c" : "Mantener o crear espacios de tratamiento de residuos. Manejo de los residuos. Desarrollar proyectos de proteccion ambiental. Capacitaciones Ambientales."},
{"u" : "140000", "o" : "1269" , "t" : "m", "n" : 2 , "c" : "Coordinaciones necesarias con el MTC para solicitar la recategorizacion de la red vecinal identificada como de importancia regional. 50% de las provincias unidas con carreteras en buen estado."},
{"u" : "140000", "o" : "1269" , "t" : "m", "n" : 2 , "c" : "Coordinar con los municipios provinciales de toda la region. 100%."},
{"u" : "140000", "o" : "1269" , "t" : "m", "n" : 2 , "c" : "50% de las provincias con espacios de tratamiento de residuos y con programas de forestacion, reforestacion y conservacion de suelos."},

{"u" : "140000", "o" : "1269" , "t" : "s", "n" : 3 , "c" : "Transparencia en el gasto publico. Difusion e informacion de gastos. Formacion de Comites de Vigilancia"},
{"u" : "140000", "o" : "1269" , "t" : "s", "n" : 3 , "c" : "Desarrollar capacitaciones a los empleados publicos y funcionarios de la Region. Simplificar los TUPAS institucionales."},
{"u" : "140000", "o" : "1269" , "t" : "s", "n" : 3 , "c" : "Fomentar el Dialogo orientado al desarrollo. Construir una vision compartida al futuro. Debe ser inclusivo (involucrar a todos los que son parte del territorio). Consultas, Encuestas, Foros, etc."},
{"u" : "140000", "o" : "1269" , "t" : "m", "n" : 3 , "c" : "Portal informativo en las Provincias de nuestra region, en un 100%."},
{"u" : "140000", "o" : "1269" , "t" : "m", "n" : 3 , "c" : "Capacitacion al 100% del personal de la region"},
{"u" : "140000", "o" : "1269" , "t" : "m", "n" : 3 , "c" : "Todo ordenamiento, zonificacion del territorio debe responder a los lineamientos y directrices del Planeamiento Estrategico"},


{"u" : "140000", "o" : "332" , "t" : "s", "n" : 0 , "c" : "Erradicar la desnutricion infantil cronica, poblacion bien alimentada y con servicios de salud modernos"},
{"u" : "140000", "o" : "332" , "t" : "s", "n" : 0 , "c" : "Eficiente Prestacion de Servicios Basicos de Saneamiento, en coordinacion con los gobiernos locales, el Ministerio de Vivienda y la cooperacion internacional"},
{"u" : "140000", "o" : "332" , "t" : "s", "n" : 0 , "c" : "Fortalecer y ampliar el desarrollo social y la igualdad de oportunidades en los grupos de poblacion vulnerableV"},
{"u" : "140000", "o" : "332" , "t" : "m", "n" : 0 , "c" : "Red de establecimientos de salud Fortalecidas. Priorizando el primer nivel de atencion. Personal que labora en el primer nivel ha sido capacitado mediante Educacion Continua, en un 60%."},
{"u" : "140000", "o" : "332" , "t" : "m", "n" : 0 , "c" : "Construccion de plantas de tratamiento de residuos solidos en las ciudades intermedias (Canete, Huacho, Huaral Barranca) y de rellenos sanitarios multi distritales en cada cuenca."},
{"u" : "140000", "o" : "332" , "t" : "m", "n" : 0 , "c" : "Crear la Casa de la Juventud, Promover la participacion organizada de la juventud en el desarrollo regional Crear 02 centros de desarrollo integral familiar, para los grupos en situacion de vulnerabilidad Fortalecer el Programa Escuela para padres"},

{"u" : "140000", "o" : "332" , "t" : "s", "n" : 1 , "c" : "consolidar a la Region Lima como el principal productor de alimentos agropecuarios fruticola del pais, en base al fortalecimiento de las Iniciativas emprendedoras y la promocion de la inversion privada en la agroindustria"},
{"u" : "140000", "o" : "332" , "t" : "s", "n" : 1 , "c" : "Modernizar y fortalecer a la Direccion Regional Agraria Creacion del Instituto Regional para la Gestion de Cuencas Mejorar la infraestructura productiva"},
{"u" : "140000", "o" : "332" , "t" : "s", "n" : 1 , "c" : "Creacion de la oficina tecnica para el desarrollo de programas de riego"},
{"u" : "140000", "o" : "332" , "t" : "m", "n" : 1 , "c" : "Proyectos para fortalecer las capacidades y asistencia tecnica para iniciativas de pequenos productores asociados. Concluir el saneamiento fisico legal de los predios rurales de toda la region Promover la acuicultura tanto maritima como continental"},
{"u" : "140000", "o" : "332" , "t" : "m", "n" : 1 , "c" : "Creacion de Centro de Innovacion, Investigacion, Certificacion y Transferencia Tecnologica Agropecuario Regional. servicios especializados y permanentes en el manejo recursos naturales a la comunidad Promover y fortalecer las cadenas de valor en los sectores agropecuarios, acuicolas, turisticos (09)"},
{"u" : "140000", "o" : "332" , "t" : "m", "n" : 1 , "c" : "Fortalecimiento, construccion de defensas de lagunas y represa, mantenimiento de canales (10 cuencas) Promover la conservacion y el uso adecuado del agua para riego en agricultura a traves del almacenamiento, conduccion y distribucion. Desarrollo del Programa Mi Riego Recuperacion de andenes"},

{"u" : "140000", "o" : "332" , "t" : "s", "n" : 2 , "c" : "Fortalecer las llamadas ciudades intermedias (Huacho, Barranca, Oyon, Canete, Huaral, Canta, Yauyos, Matucana, etc)"},
{"u" : "140000", "o" : "332" , "t" : "s", "n" : 2 , "c" : "Definir los limites territoriales de cada una de las circunscripciones de nuestra region, disminuyendo los conflictos a nivel departamental, regional, provincial y distrital"},
{"u" : "140000", "o" : "332" , "t" : "s", "n" : 2 , "c" : "Construir y fortalecer corredores integrales: economicos, sociales y culturales, en base a las cuencas de los rios"},
{"u" : "140000", "o" : "332" , "t" : "m", "n" : 2 , "c" : "Planes de desarrollo urbano rural, promotor del emprendimiento, con servicios basicos modernos de saneamiento, transporte y comercio"},
{"u" : "140000", "o" : "332" , "t" : "m", "n" : 2 , "c" : "Saneamiento de los limites en la Region Lima"},
{"u" : "140000", "o" : "332" , "t" : "m", "n" : 2 , "c" : "7 Corredores organizados sobre la base de las cuencas hidrograficas Provincias y centros de produccion de las cuencas, articulados con las ciudades intermedias de otras regiones como Pasco, Huanuco, Pucallpa y la megaciudad de Lima Metropolitana-Callao"},

{"u" : "140000", "o" : "332" , "t" : "s", "n" : 3 , "c" : "Promover la profundizacion del proceso de descentralizacion, desde la ANGR, en alianza estrategica con AMPE y REMURPE, incidiendo en la descentralizacion fiscal."},
{"u" : "140000", "o" : "332" , "t" : "s", "n" : 3 , "c" : "Diseno participativo de politicas publicas regionales, en el marco de la participacion ciudadana y procesos sociales."},
{"u" : "140000", "o" : "332" , "t" : "s", "n" : 3 , "c" : "Estructura organico funcional, articulado a las nuevas tendencias y necesidades geopoliticas de la Region Lima."},
{"u" : "140000", "o" : "332" , "t" : "m", "n" : 3 , "c" : "Se han elaborado propuestas de incidencia politica ante entidades gubernamentales."},
{"u" : "140000", "o" : "332" , "t" : "m", "n" : 3 , "c" : "Politicas publicas aprobadas y en curso de aplicacion."},
{"u" : "140000", "o" : "332" , "t" : "m", "n" : 3 , "c" : "Estructura organica administrativa, en funcionamiento, evaluada y monitoreada."},


{"u" : "140000", "o" : "2160" , "t" : "s", "n" : 0 , "c" : "Gestionar ante el Ministerio de Educacion la cobertura educativa requerida"},
{"u" : "140000", "o" : "2160" , "t" : "s", "n" : 0 , "c" : "Mejoramiento,Mantenimiento y Equipamiento de Instituciones Educativas."},
{"u" : "140000", "o" : "2160" , "t" : "s", "n" : 0 , "c" : "Implementacion de Puestos de Salud con Personal Profesional, Medicinas y Equipamiento."},
{"u" : "140000", "o" : "2160" , "t" : "m", "n" : 0 , "c" : "Coberturar un 80% de Instituciones Educativas mediante la gestion al finalizar el gobierno"},
{"u" : "140000", "o" : "2160" , "t" : "m", "n" : 0 , "c" : "Un 60 % de Instituciones Educativas mejoradas, mantenidas y equipadas."},
{"u" : "140000", "o" : "2160" , "t" : "m", "n" : 0 , "c" : "Coberturar en 80% en atencion Medica, Medicinas y Equipamiento de los Puestos de Salud."},

{"u" : "140000", "o" : "2160" , "t" : "s", "n" : 1 , "c" : "Implementacion de Proyectos Productivos agropecuarios para mejorar las condiciones de vida de la poblacion"},
{"u" : "140000", "o" : "2160" , "t" : "s", "n" : 1 , "c" : "Utilizacion de las lagunas y cuencas para Proyectos de Criaderos de Truchas como mejor alimento y crecimiento economico de la Poblacion."},
{"u" : "140000", "o" : "2160" , "t" : "s", "n" : 1 , "c" : "Capacitacion y Asistencia Tecnica con el uso de Tecnologias innovadoras para lograr su Desarrollo."},
{"u" : "140000", "o" : "2160" , "t" : "m", "n" : 1 , "c" : "Apoyo directo a los Productores Agropecuarios en un 80%."},
{"u" : "140000", "o" : "2160" , "t" : "m", "n" : 1 , "c" : "Hasta un 80 % de las Fuentes de Agua utilizadas en Piscigranjas para la Alimentacion."},
{"u" : "140000", "o" : "2160" , "t" : "m", "n" : 1 , "c" : "Cobertura en 70 % con Capacitacion y Asistencia Tecnica."},

{"u" : "140000", "o" : "2160" , "t" : "s", "n" : 2 , "c" : "desarrollar e Impulsar Mega Proyectos de Puertos y Aeropuertos."},
{"u" : "140000", "o" : "2160" , "t" : "s", "n" : 2 , "c" : "Desarrollar e Impulsar el Proyecto Ferroviario Costero de la Region: Ciudades de Barranca, Huaura, Huaral, Lima y Canete."},
{"u" : "140000", "o" : "2160" , "t" : "s", "n" : 2 , "c" : "Construir Represas y Acueductos que aseguren la Provision de Agua a la Region."},
{"u" : "140000", "o" : "2160" , "t" : "m", "n" : 2 , "c" : "Estudios oficiales de los Proyectos Mega Puerto en la Bahia El Paraiso Punta Salinas- Huacho y el Mega Aeropuerto en la Zona El Paraiso- Huacho."},
{"u" : "140000", "o" : "2160" , "t" : "m", "n" : 2 , "c" : "Estudios del Proyecto Ferroviario: Barranca, HUaura, Huaral, Lima y Canete."},
{"u" : "140000", "o" : "2160" , "t" : "m", "n" : 2 , "c" : "Construccion de 4 Represas en las Cuencas Hidricas de la Region"},

{"u" : "140000", "o" : "2160" , "t" : "s", "n" : 3 , "c" : "Reestructuracion de la Administracion Regional en busca de Eficiencia, Eficacia y Competitividad."},
{"u" : "140000", "o" : "2160" , "t" : "s", "n" : 3 , "c" : "Disenar el Perfil y Procesos de seleccion Transparente y Capacitacion Especializada al Personal Trabajador."},
{"u" : "140000", "o" : "2160" , "t" : "s", "n" : 3 , "c" : "Ejecutar Procesos transparentes y Legales en las licitaciones de Obras y Adquisiciones de Bienes y Servicios."},
{"u" : "140000", "o" : "2160" , "t" : "m", "n" : 3 , "c" : "Lograr la Eficiencia en el 70% del Personal trabajador de la Region."},
{"u" : "140000", "o" : "2160" , "t" : "m", "n" : 3 , "c" : "Lograr que el 90% del personal Trabajador sea Profesionalmente seleccionado y Capacitado."},
{"u" : "140000", "o" : "2160" , "t" : "m", "n" : 3 , "c" : "100% de las Licitaciones Legales y Transparentes."},


{"u" : "140000", "o" : "22" , "t" : "s", "n" : 0 , "c" : "Fortalecer la atencion integral de la salud en redes, superando la debilidad de atencion primaria, mejorando los Recursos Humanos en cantidad y calidad, mejorando la infraestructura y el equipamiento. Paralelamente se pretende implantar un sistema de control que garantice una atencion adecuada."},
{"u" : "140000", "o" : "22" , "t" : "m", "n" : 0 , "c" : "Disminuir el 33% de indices de morbilidad y mortalidad materno infantil en la Region"},

{"u" : "140000", "o" : "22" , "t" : "s", "n" : 1 , "c" : "La gestion pretende promocionar mediante PROGRAMAS DE CAPACITACION EMPRENDEDORA, para que los actores economicos, especialmente las MYPES adquieran alta competitividad y puedan GENERAR EMPLEO"},
{"u" : "140000", "o" : "22" , "t" : "m", "n" : 1 , "c" : "Disminuir la informalidad en un 33% y el desempleo en un 20%"},

{"u" : "140000", "o" : "22" , "t" : "s", "n" : 2 , "c" : "Para solucionar la contaminacion en los rios, se propone que el manejo sea por Cuencas Hidrograficas en toda la Region Lima Provincias, con participacion responsable de todos los involucrados."},
{"u" : "140000", "o" : "22" , "t" : "m", "n" : 2 , "c" : "1.- El 1° ano del nuevo Gobierno Regional, se instalaran las Comisiones Ejecutivas en todas las Cuencas Hidrograficas de toda la Region. 2.- El 2° ano se tendra aprobado el Plan de Desarrollo de cada Cuenca Hidrografica. 3.- El 3° ano se dara inicio al PLAN DE ACCION en cada Cuenca Hidrograficas"},

{"u" : "140000", "o" : "22" , "t" : "s", "n" : 3 , "c" : "1°Lograr que todo el personal asuma su rol con VOCACION DE SERVICIO y teniendo presente la importancia de su puesto de trabajo en el DESARROLLO DE NUESTRA REGION. 2°Capacitar al personal para que asuma sus funciones en forma adecuada. 3°Controlar al personal en el cumplimiento de sus funciones"},
{"u" : "140000", "o" : "22" , "t" : "m", "n" : 3 , "c" : "Al termino del 1° ano de la gestion, se pretende que el 100% del personal de la Entidad, este enteramente MOTIVADO en el cumplimiento de sus funciones e IDENTIFICADO con el DESARROLLO de la Region."},


{"u" : "140000", "o" : "1264" , "t" : "s", "n" : 0 , "c" : "PROGRAMA DE MEJORAMIENTO DE LA CAPACIDAD RESOLUTIVA DE LOS SERVICIOS DE SALUD EN LAS NUEVE PROVINCIAS DE LA REGION. EQUIPAMIENTO MEDICO Y MEJOR DISPOSICION DE PROFESIONAL ASISTENCIAL"},
{"u" : "140000", "o" : "1264" , "t" : "s", "n" : 0 , "c" : "PROGRAMA DE MEJORAMIENTO DE LA CALIDAD Y COBERTURA DE LOS SERVICIOS PUBLICOS DE EDUCACION EN LAS NUEVE PROVINCIAS DE LA REGION. EQUIPAMIENTO EDUCATIVO Y DE INFRAESTRUCTURA"},
{"u" : "140000", "o" : "1264" , "t" : "s", "n" : 0 , "c" : "PROGRAMA DE LIDERAZGO Y DESARROLLO DE CAPACIDADES DE LAS ORGANIZACIONES SOCIALES Y DE SOCIEDAD CIVIL. ESTE PROGRAMA INCLUYE COMPONENTES DE FORMACION, DE ORGANIZACION Y DE PROMOCION DE LIDERAZGOS CIUDADANOS."},
{"u" : "140000", "o" : "1264" , "t" : "m", "n" : 0 , "c" : "09 Establecimientos de Salud mejor equipados y con infraestructura adecuada para mejor cobertura (uno por Provincia)"},
{"u" : "140000", "o" : "1264" , "t" : "m", "n" : 0 , "c" : "09 Instituciones Educativas mejor equipados y con infraestructura adecuada para mejor cobertura (uno por Provincia) / 09 PIP SNIP"},
{"u" : "140000", "o" : "1264" , "t" : "m", "n" : 0 , "c" : "1,000 Lideres sociales (varones y mujeres) principalmente jovenes de las nueve provincias de Lima estaran en condiciones de ejercer su ciudadania en roles de vigilancia, cogestion, participacion e interlocucion social ante las entidades publicas y de gobierno local y regional."},

{"u" : "140000", "o" : "1264" , "t" : "s", "n" : 1 , "c" : "PROGRAMA REGIONAL AGRICULTORES PARA EL DESARROLLO Programa Regional que otorgara creditos agricolas en alianza con entidades publicas y privadas. Este programa brindara asistencia tecnica para mejorar."},
{"u" : "140000", "o" : "1264" , "t" : "s", "n" : 1 , "c" : "CREAR FONDO DE GARANTIAS FONDO PARA EMPRENDEDORES, Constituir un Fondo de Garantias para financiar micro proyectos en los campos de la gastronomia, el turismo ecologico, turismo de aventura u otras ideas de negocios."},
{"u" : "140000", "o" : "1264" , "t" : "s", "n" : 1 , "c" : "PROGRAMA MAESTRO DE MEJORAMIENTO DE LOS MERCADOS MINORISTAS Y MAYORISTAS DE LAS PROVINCIAS DE HUARAL, HUAURA, CANETE Y BARRANCA. Se declarara de interes regional que las inversiones del gobierno regional esten orientadas a mejorar la infraestructura, seguridad, calidad del comercio."},
{"u" : "140000", "o" : "1264" , "t" : "m", "n" : 1 , "c" : "5 Millones de Nuevos Soles otorgados en Creditos Agricolas"},
{"u" : "140000", "o" : "1264" , "t" : "m", "n" : 1 , "c" : "2millones de Dolares disponibles"},
{"u" : "140000", "o" : "1264" , "t" : "m", "n" : 1 , "c" : "04 Mercados Minoristas y Mayoristas disponibles y operativos en Huaral, Barranca, Huaura y Canete. Habran mejorado su infraestructura, Calidad de Productos y la Seguridad."},

{"u" : "140000", "o" : "1264" , "t" : "s", "n" : 2 , "c" : "PROYECTO DE APOYO EN EQUIPAMENTO TECNICO TECNOLOGICO Y DE GESTION A LAS UNIDADES PUBLICAS RECTORAS EN EVALUACION, CONTROL Y MONITOREO AMBIENTAL PROYECTO DE FORTALECIMIENTO DE LA CAPACIDAD DE CONTROL SOCIAL EN LOS FOCOS DE ALTO RIESGO AMBIENTAL REGIONAL"},
{"u" : "140000", "o" : "1264" , "t" : "s", "n" : 2 , "c" : "PLAN MAESTRO DE ARTICULACION VIAL CON PROYECTOS DE CARRETERAS DE PENETRACION TRANSVERSAL Y DE ALTERNANCIA A LA PANAMERICANA"},
{"u" : "140000", "o" : "1264" , "t" : "s", "n" : 2 , "c" : "PROYECTOS DE INVERSION BAJO EL MECANISMO DE ALIANZAS PUBLICO PRIVADO – APP QUE DOTEN A LAS 4 PROVINCIAS DE LA COSTA Y LA PROVINCIA DEHUAROCHIRI DE TERMINALES INTERPROVINCIALES SEGUROS, CON CONFORT Y DE ALTA CALIDAD"},
{"u" : "140000", "o" : "1264" , "t" : "m", "n" : 2 , "c" : "02 PROYECTOS DE INVERSION PUBLICA QUE INSTALEN CAPACIDADES DE RESPUESTA INSTITUCIONAL AMBIENTAL EN EL CUIDADO DE LA SALUD Y SUSTENTABILIDAD AMBIENTAL"},
{"u" : "140000", "o" : "1264" , "t" : "m", "n" : 2 , "c" : "-	APOYO EN GESTION DE TERMINACION DE CARRETERA ACOS ANTAJIRCA HUALLAY - PROYECTO DE CARRETERA ALTERNA A PANAMERICANA NORTE TRAMO HUARAL, HUACHO, BARRANCA -	GESTION EN MEJORA DE CONDICIONES DE CONCESION DE TRAMO PANAMERICANA DOTANDOLA DE SEGURIDAD Y CALIDAD"},
{"u" : "140000", "o" : "1264" , "t" : "m", "n" : 2 , "c" : "05 TERMINALES INTERPROVINCIALES (BARRANCA, HUAURA, HUARAL, HUAROCHIRI Y CANETE)"},

{"u" : "140000", "o" : "1264" , "t" : "s", "n" : 3 , "c" : "REESTRUCTURACION DEL GOBIERNO REGIONAL, CREANDO SUB SEDES REGIONAL DE ZONA NOR ESTE Y ZONA SUR ESTE DE LA REGION."},
{"u" : "140000", "o" : "1264" , "t" : "s", "n" : 3 , "c" : "PROGRAMA DE FISCALIZACION INTERGUBERNAMENTAL DE LOS PROCESOS DE CONTRATACIONES Y ADQUISICIONES. Estableceremos convenios con organismos de fiscalizacion y supervisor que garantice “Cero Corrupcion”,"},
{"u" : "140000", "o" : "1264" , "t" : "s", "n" : 3 , "c" : "PROGRAMA DE DESARROLLO DE COMPETENCIAS EN GESTION PUBLICA PARA FUNCIONARIOS DE GOBIERNO REGIONAL Y MUNICIPAL. ESTE PROGRAMA DE DESARROLLO DE CAPACIDADES ESTA CENTRADO EN BRINDAR ACCESO A LOS FUNCIONARIOS PUBLICOS DE LA REGION A UN PROCESO CONTINUO DE CAPACITACION"},
{"u" : "140000", "o" : "1264" , "t" : "m", "n" : 3 , "c" : "PROYECTOS DE INVERSION PUBLICA CON MEJORES RATIOS DE COSTO BENEFICIO Y CON CRITERIO DE COSTO SOCIAL ZONAL"},
{"u" : "140000", "o" : "1264" , "t" : "m", "n" : 3 , "c" : "LOS PROCESOS DE CONTRATACIONES Y ADQUISICIONES DISPONDRAN DE ACTA DE TRANSPARENCIA POR HABER SIDO SUPERVISADAS POR ORGANISMOS DE CONTROL Y VIGILANCIA SOCIAL INTERGUBERNAMENTAL."},
{"u" : "140000", "o" : "1264" , "t" : "m", "n" : 3 , "c" : "800 PROFESIONALES DE GOBIERNO REGIONAL Y DE GOBIERNOS LOCALES HABRAN DESARROLLADO MEJORES NIVELES DE DESEMPENO TECNICO Y SOCIAL."},


{"u" : "140000", "o" : "1257" , "t" : "s", "n" : 0 , "c" : "•	Amplias clases medias y sectores altos y bajos reducidos (forma romboidal de la estructura de ingresos). •	Democracias representativas y participativas, con sociedades abiertas, flexibles y transparentes. •	Modernizacion de la economia de mercado."},
{"u" : "140000", "o" : "1257" , "t" : "s", "n" : 0 , "c" : "•	Garantizar el respeto irrestricto y la vigencia de los derechos fundamentales. •	Impulsar el desarrollo de la legislacion secundaria que haga operativos los derechos fundamentales. •	Erradicar todas las formas de trabajo infantil y adolescente que ponen en riesgo la integridad."},
{"u" : "140000", "o" : "1257" , "t" : "s", "n" : 0 , "c" : "•	Nos comprometemos a dar prioridad efectiva a la lucha contra la pobreza y a la reduccion de la desigualdad social, aplicando politicas integrales y mecanismos orientados a garantizar la igualdad de oportunidades economicas, sociales y politicas."},
{"u" : "140000", "o" : "1257" , "t" : "m", "n" : 0 , "c" : "La democracia, concebida como la convivencia social en la que todos sus miembros son libres e iguales y las relaciones sociales se establecen de acuerdo con mecanismos contractuales, y fortalecida por la consolidacion del Estado de derecho y la mayor participacion de la sociedad civil."},
{"u" : "140000", "o" : "1257" , "t" : "m", "n" : 0 , "c" : "•	Fortalecer las instituciones vinculadas a la administracion de justicia. •	Asegurar el acceso gratuito a la justicia a las poblaciones afectadas por la pobreza y la pobreza extrema. •	Fortalecer la independencia e imparcialidad del sistema de justicia social."},
{"u" : "140000", "o" : "1257" , "t" : "m", "n" : 0 , "c" : "Que todas las personas tengan igualdad de oportunidades para desarrollarse, lo que implica tener acceso a servicios basicos de calidad, en particular educacion, salud, agua y desagüe, electricidad, telecomunicaciones, vivienda y seguridad ciudadana."},

{"u" : "140000", "o" : "1257" , "t" : "s", "n" : 1 , "c" : "•	La focalizacion de hogares es parte de los objetivos para mejorar la calidad del gasto publico. En el 2004 se establecieron los criterios y mecanismos para mejorar la equidad y calidad en el gasto social y focalizarlo, dando prioridad a la atencion de los mas pobres."},
{"u" : "140000", "o" : "1257" , "t" : "s", "n" : 1 , "c" : "•	Nos comprometemos a desarrollar una integral descentralizacion politica, economica y administrativa, transfiriendo progresivamente competencias y recursos del gobierno regional a los gobiernos locales provincial y distrital, con el fin de eliminar el centralismo."},
{"u" : "140000", "o" : "1257" , "t" : "s", "n" : 1 , "c" : "•	La falta de fortalecimiento a las industrias regionales orientadas al mercado interno y promover su participacion en los mercados internacionales."},
{"u" : "140000", "o" : "1257" , "t" : "m", "n" : 1 , "c" : "•	Que todas las personas tengan igualdad de oportunidades para desarrollarse, lo que implica tener acceso a servicios basicos de calidad, en particular educacion, salud, agua y desagüe, electricidad, telecomunicaciones, vivienda y seguridad ciudadana."},
{"u" : "140000", "o" : "1257" , "t" : "m", "n" : 1 , "c" : "•	Apoyara el fortalecimiento administrativo y financiero del gobierno regional y locales. •	Institucionalizara la participacion ciudadana en las decisiones politicas, economicas y administrativas."},
{"u" : "140000", "o" : "1257" , "t" : "m", "n" : 1 , "c" : "•	Mantener la continuidad del crecimiento economico. •	Desarrollar la ciencia y la tecnologia aplicadas al logro del desarrollo sostenible."},

{"u" : "140000", "o" : "1257" , "t" : "s", "n" : 2 , "c" : "•	Debido a la situacion descrita, el desarrollo regional esta condicionado a la conformacion de escenarios de integracion sobre la base de criterios de ordenamiento territorial que permitan a la dinamica social, economica y ambiental converger de manera sostenible."},
{"u" : "140000", "o" : "1257" , "t" : "s", "n" : 2 , "c" : "•	Debe senalarse que se tiene un conocimiento limitado sobre el valor de los servicios ecosistemicos, es decir, de los beneficios que la poblacion obtiene de los ecosistemas. Algunos de esos beneficios son directos, como la provision de agua y alimentos."},
{"u" : "140000", "o" : "1257" , "t" : "s", "n" : 2 , "c" : "•	Proteger el ambiente y sus componentes con enfoque preventivo y recuperar la calidad ambiental, asegurando la conservacion y el aprovechamiento sostenible de los recursos naturales y la biodiversidad de una manera responsable y congruente con el respeto de los derechos fundamentales de las persona"},
{"u" : "140000", "o" : "1257" , "t" : "m", "n" : 2 , "c" : "•	Establecer en los espacios transversales de planificacion macrorregional la red de corredores economicos interoceanicos, asi como de las vias longitudinales de la costa, sierra y selva, de forma que sustenten la adecuada distribucion y ocupacion poblacional del territorio cautelando las fronteras"},
{"u" : "140000", "o" : "1257" , "t" : "m", "n" : 2 , "c" : "•	Impulsar la evaluacion y la valoracion del patrimonio natural e integrarlas en la planificacion del desarrollo. •	Impulsar la gestion integrada de los recursos naturales, la gestion integrada de los recursos hidricos y el ordenamiento territorial."},
{"u" : "140000", "o" : "1257" , "t" : "m", "n" : 2 , "c" : "•	Adaptacion del pais al cambio climatico. •	Implementar el Sistema Nacional de Gestion Ambiental. •	Programa Inventario y valoracion de recursos naturales a nivel nacional"},

{"u" : "140000", "o" : "1257" , "t" : "s", "n" : 3 , "c" : "•	Deficit administrativo completo. •	Crisis en la administracion de los recursos. •	Crisis en la politica administrativas de las facultades adquiridas. •	Mala administracion publica."},
{"u" : "140000", "o" : "1257" , "t" : "s", "n" : 3 , "c" : "•	Tiene lugar cuando se producen los cambios en las formas e instrumentos de gobernar. Es el nivel estricto del redimensionamiento de la administracion regional, la reduccion de su tamano, la disminucion del numero de programas, empleados, leyes, gasto, etc."},
{"u" : "140000", "o" : "1257" , "t" : "s", "n" : 3 , "c" : "•	Definir nuevas reglas de juego y aumentar la capacidad de gobernabilidad del gobierno regional mediante medidas fiscales, sistema de elecciones, representatividad en los espacios de participacion, etc."},
{"u" : "140000", "o" : "1257" , "t" : "m", "n" : 3 , "c" : "•	Reestructurara la administracion publica regional en su totalidad. •	Mirar los nuevos esquemas de desarrollo sistematizado para garantizar una eficaz administracion."},
{"u" : "140000", "o" : "1257" , "t" : "m", "n" : 3 , "c" : "•	Tener al final las reformas vinculadas a la relacion administrativa, politica entre sociedad y el Gobierno Regional, en particular la forma de elegir y las formas como se componen y ejercen los poderes publicos. Tambien las formas de interrelacion entre los poderes y niveles del gobierno local."},
{"u" : "140000", "o" : "1257" , "t" : "m", "n" : 3 , "c" : "•	Cambiar las funciones del gobierno regional o de determinadas unidades organicas que lo conforman, mediante cambios significativos en la estructura del Estado que alteran su funcionamiento para poder responder mejor a las demandas de la poblacion."},


{"u" : "140000", "o" : "553" , "t" : "s", "n" : 0 , "c" : "Inversion masiva en proyectos de saneamiento y electrificacion enmarcadas dentro del presupuesto participativo regional. Con proyectos de almacenamiento del recurso hidrico"},
{"u" : "140000", "o" : "553" , "t" : "s", "n" : 0 , "c" : "Continuar con los programas regionales para mejorar las herramientas y tecnologia en colegios e institutos. Mejorar la infraestructura hospitales y centros de salud"},
{"u" : "140000", "o" : "553" , "t" : "s", "n" : 0 , "c" : "Implementacion y equipamiento adecuado a los Comedores Escolares existentes en las 9 provincias de nuestra region. •	La implementacion de bibliotecas virtuales accesibles y modulos de terapia de lenguaje para los Centros Educativos Basicos Especiales"},
{"u" : "140000", "o" : "553" , "t" : "m", "n" : 0 , "c" : "Reducir los indices de hogares sin acceso a los servicios basicos de agua potable, alcantarillado y energia electrica."},
{"u" : "140000", "o" : "553" , "t" : "m", "n" : 0 , "c" : "Mejorar los niveles de comprension lectora y razonamiento matematico. Brindar acceso a eficientes servicios educativos y de salud"},
{"u" : "140000", "o" : "553" , "t" : "m", "n" : 0 , "c" : "Mejores condiciones a las personas con discapacidad y ninos atendidos nutricionalmente en las instituciones educativas."},

{"u" : "140000", "o" : "553" , "t" : "s", "n" : 1 , "c" : "Con la finalidad de lograr una informacion estadistica real de mercados para saber que producir en nuestra region crearemos un DEPARTAMENTO TECNICO DE ESTADISTICA REGIONAL, que acopie informacion nacional e internacional ofreciendo una orientacion valiosa de oportunidades para nuestros productos."},
{"u" : "140000", "o" : "553" , "t" : "s", "n" : 1 , "c" : "Continuaremos con la programacion del proyecto MEJORAMIENTO GENETICO DEL GANADO, Y AGROPECUARIO. Continuaremos con el programa exitoso de CANALIZACION DE REGADIOS. En un trabajo articulado con las juntas de usuarios."},
{"u" : "140000", "o" : "553" , "t" : "s", "n" : 1 , "c" : "impulsaremos la ORGANIZACION DE LOS AGRICULTORES, PESCADORES Y GANADEROS (Comites de productores, juntas de usuarios, comites de ganaderos en todas sus formas (cadenas productivas) con la asesoria tecnica y capacitacion por parte de la Region."},
{"u" : "140000", "o" : "553" , "t" : "m", "n" : 1 , "c" : "Con ello alcanzaremos mejores niveles de produccion en nuestros valles, fomentaremos el empleo, y garantizaremos la alimentacion de la poblacion, con productos de consumo interno y de exportacion."},
{"u" : "140000", "o" : "553" , "t" : "m", "n" : 1 , "c" : "Mejorar los ingresos de las familias ganaderas y agropecuarias. Se elevaran los niveles de produccion, y habra un mejor aprovechamiento del recurso hidrico."},
{"u" : "140000", "o" : "553" , "t" : "m", "n" : 1 , "c" : "Organizaciones fortalecidas, con liderazgo regional y nacional, que articular de manera ordenada sus proyectos y negocios, con un mercado clave para sus ingresos economicos."},

{"u" : "140000", "o" : "553" , "t" : "s", "n" : 2 , "c" : "Fortalecer la autoridad ambiental, desconcentrando decisiones ambientales, y promoveremos: Plantas de Tratamiento de Residuos Solidos organicos e inorganicos, y Centros Demostrativos Ambientales en cada provincia de la region."},
{"u" : "140000", "o" : "553" , "t" : "s", "n" : 2 , "c" : "•	Seguiremos impulsando la construccion de las principales carreteras de integracion como lo es la Carretera Sayan – Churin; Imperial – Yauyos; Lima - Canta. •	Impulsar la construccion de vias de evitamiento de transporte pesado en las ciudades de las 9 provincias de nuestra region."},
{"u" : "140000", "o" : "553" , "t" : "s", "n" : 2 , "c" : "a) Impulsar la Construccion del Mega –Aeropuerto Internacional Las Salinas - Huacho b) Carretera Interoceanica IIRSA Centro – Variante R16 c) Mega – Puerto de Bahia las Salinas – Huacho"},
{"u" : "140000", "o" : "553" , "t" : "m", "n" : 2 , "c" : "Lograr que cada provincia lidere en gestion ambiental, con infraestructura que permite el aprovechamiento sostenible de los residuos y controla el dano ambiental"},
{"u" : "140000", "o" : "553" , "t" : "m", "n" : 2 , "c" : "Nuestra region se encontrara articulada entre provincias y departamentos vecinos."},
{"u" : "140000", "o" : "553" , "t" : "m", "n" : 2 , "c" : "Nuestra region sera eje del desarrollo de la zona central del pais, articulada desde el Pacifico al Atlantico"},

{"u" : "140000", "o" : "553" , "t" : "s", "n" : 3 , "c" : "En esta oportunidad tenemos la obligacion de la renovacion funcional y ejecutiva de las Oficinas Zonales de Participacion y Concertacion, en organos de linea, que viabilicen la ejecucion de proyectos de inversion publica, con personal humano debidamente calificado."},
{"u" : "140000", "o" : "553" , "t" : "s", "n" : 3 , "c" : "Continuaremos promoviendo las audiencias publicas descentralizadas en las 9 provincias de la Region."},
{"u" : "140000", "o" : "553" , "t" : "s", "n" : 3 , "c" : "Vamos a continuar la adquisicion de un pool de maquinarias: cargador frontal, cisterna y niveladora a cada una de las 9 provincias. (Como referencia a la redefinicion de las oficinas zonales)"},
{"u" : "140000", "o" : "553" , "t" : "m", "n" : 3 , "c" : "Tener un gobierno integrado con sus dependencias y unidades ejecutoras."},
{"u" : "140000", "o" : "553" , "t" : "m", "n" : 3 , "c" : "Un gobierno regional transparente con una ciudadania conocedora de como se invierte y en que se invierte."},
{"u" : "140000", "o" : "553" , "t" : "m", "n" : 3 , "c" : "provincias atendidas en gestion de riesgos y defensas riberenas."},


{"u" : "140000", "o" : "46" , "t" : "s", "n" : 0 , "c" : "La Revolucion de la Educacion requiere el esfuerzo conjunto del Estado, maestros, padres de familia, estudiantes y sociedad civil, actuando e interviniendo en todos los niveles educativos: Inicial, Basica, Tecnica y Superior."},
{"u" : "140000", "o" : "46" , "t" : "s", "n" : 0 , "c" : "Proponemos un modelo de Salud integral e incluyente, que mejore el acceso y la atencion de salud de calidad, con equidad y trato digno para toda la poblacion, especialmente los grupos vulnerables (madres, ninos, discapacitados, comunidades campesinas, grupos excluidos y la tercera edad)."},
{"u" : "140000", "o" : "46" , "t" : "s", "n" : 0 , "c" : "El objetivo es aumentar la competitividad agricola para el mercado, para lo cual desarrollaremos un programa para el sostenimiento de la ganaderia y la agricultura de los pequenos productores alto-andinos, promoviendo la agricultura organica dado su mejor precio en el mercado."},
{"u" : "140000", "o" : "46" , "t" : "m", "n" : 0 , "c" : "Reducir en un 10% el analfabatismo de la situacion actual."},
{"u" : "140000", "o" : "46" , "t" : "m", "n" : 0 , "c" : "Equipar optimamente equipados con centros quirurgicos en todo el pais. Elevar la categoria de centros de salud via un adecuado equipamiento y con el personal necesario. Reducir la mortalidad materna."},
{"u" : "140000", "o" : "46" , "t" : "m", "n" : 0 , "c" : "Duplicar la produccion. El agro regional crecera en la region en 5% anual en su contribucion al PIB. Invertir en infraestructura agricola para mejorar los proyectos de irrigacion en la costa y sierra."},

{"u" : "140000", "o" : "46" , "t" : "s", "n" : 1 , "c" : "Es necesario pasar de las reformas y el crecimiento economico al desarrollo productivo con generacion de empleo, superando la etapa extractiva de recursos naturales y orientando los esfuerzos hacia la transformacion productiva con valor agregado."},
{"u" : "140000", "o" : "46" , "t" : "s", "n" : 1 , "c" : "Diversificar los destinos turisticos mejorando la infraestructura de transportes y acceso a los nuevos destinos, promoviendo los circuitos turisticos."},
{"u" : "140000", "o" : "46" , "t" : "s", "n" : 1 , "c" : "Inicio de Obras de Gran envergadura para el Gobierno Regional de Lima."},
{"u" : "140000", "o" : "46" , "t" : "m", "n" : 1 , "c" : "Implementar el programa “Megaproyectos productivos” creando conglomerados productivos por zona geografica orientados a conseguir saltos cualitativos en los PBI regionales, articulando actores publicos y privados."},
{"u" : "140000", "o" : "46" , "t" : "m", "n" : 1 , "c" : "Promover la creacion de infraestructura hotelera en el interior de la region y alrededor de los circuitos turisticos."},
{"u" : "140000", "o" : "46" , "t" : "m", "n" : 1 , "c" : "asfaltar las vias de comunicacion para penetrar con facilidad a las regiones de Huanuco y otros."},

{"u" : "140000", "o" : "46" , "t" : "s", "n" : 2 , "c" : "Lograr una economia sostenible, que garantice un medio ambiente saludable para todos, La conservacion y manejo sostenible de la biodiversidad debe ser reconocida como un componente fundamental del ambiente."},
{"u" : "140000", "o" : "46" , "t" : "s", "n" : 2 , "c" : "Recuperacion y Rehabilitacion de andenes."},
{"u" : "140000", "o" : "46" , "t" : "s", "n" : 2 , "c" : "Promover la Inversion Privada en la concesion de carreteras, aeropuertos, puertos, ferrocarriles y telecomunicaciones."},
{"u" : "140000", "o" : "46" , "t" : "m", "n" : 2 , "c" : "Cuatro son los temas centrales que deben de ser priorizados para poder avanzar: a) el agua y su gestion y manejo a nivel de cuencas) los bosques, gestion y manejo, y transformacion moderna c) el ordenamiento territorial y d) el manejo de riesgos relacionados al cambio climatico."},
{"u" : "140000", "o" : "46" , "t" : "m", "n" : 2 , "c" : "Rehabilitacion en un 5% durante la gestion."},
{"u" : "140000", "o" : "46" , "t" : "m", "n" : 2 , "c" : "Carretera de penetracion hacia el departamento de Huanuco Oyon, Raura, Lauricocha,Huanuco, Ucayali."},

{"u" : "140000", "o" : "46" , "t" : "s", "n" : 3 , "c" : "Nos proponemos fortalecer el proceso de Descentralizacion para un desarrollo inclusivo con niveles de Gobierno articulados y comprensivos de las necesidades y expectativas de los ciudadanos peruanos."},
{"u" : "140000", "o" : "46" , "t" : "s", "n" : 3 , "c" : "Apoyo a la promocion de la inversion privada en regiones y localidades. Constituir espacio de articulacion entre sector privado y publico para establecer la agenda plurianual de la Competitividad Territorial. Diseno e implementacion de politica nacional y regional de innovacion y tecnologia."},
{"u" : "140000", "o" : "46" , "t" : "s", "n" : 3 , "c" : "Acercar a los representantes hacia a sus representados mejorando la representacion politica: local, regional, nacional y supranacional. Cuotas para determinadas poblaciones excluidas."},
{"u" : "140000", "o" : "46" , "t" : "m", "n" : 3 , "c" : "Realizar evaluacion periodica."},
{"u" : "140000", "o" : "46" , "t" : "m", "n" : 3 , "c" : "evaluacion periodiodica."},
{"u" : "140000", "o" : "46" , "t" : "m", "n" : 3 , "c" : "Realizar evaluacion."},


{"u" : "140000", "o" : "1366" , "t" : "s", "n" : 0 , "c" : "Implementacion de Escuelas Saludables, para integrar la salud en las actividades cotidianas de la escuela, estableciendo objetivos realistas de promocion de la salud sobre la base de un diagnostico preciso y de la evidencia cientifica disponible sobre los temas de salud."},
{"u" : "140000", "o" : "1366" , "t" : "s", "n" : 0 , "c" : "Construccion de polideportivo, estadio, coliseo cerrado, piscina olimpica, con canchas de calentamiento y canchas multiusos para voley y basquetball."},
{"u" : "140000", "o" : "1366" , "t" : "s", "n" : 0 , "c" : "Construccion de un Centro de Rehabilitacion, con Programas de Prevencion y Tratamiento de consumidores de drogas."},
{"u" : "140000", "o" : "1366" , "t" : "m", "n" : 0 , "c" : "Reducir la desnutricion cronica y anemia en ninos entre 6 y 11 anos"},
{"u" : "140000", "o" : "1366" , "t" : "m", "n" : 0 , "c" : "Polideportivo con Estadio, Coliseo cerrado y piscina olimpica."},
{"u" : "140000", "o" : "1366" , "t" : "m", "n" : 0 , "c" : "Centro de Rehabilitacion de consumidores de Drogas."},

{"u" : "140000", "o" : "1366" , "t" : "s", "n" : 1 , "c" : "Incentivar la construccion de infraestructura hotelera y comercial para consolidar a Chancay como destino turistico, atractiva a las empresas prestadoras de servicios turisticos. Impulso al rescate arqueologico."},
{"u" : "140000", "o" : "1366" , "t" : "s", "n" : 1 , "c" : "Construccion del mercado Municipal, financiado con una alianza publico privada."},
{"u" : "140000", "o" : "1366" , "t" : "s", "n" : 1 , "c" : "Construccion de Piscigranjas con jaulas flotantes en el mar, como plan piloto con proyeccion de produccion a escala comercial."},
{"u" : "140000", "o" : "1366" , "t" : "m", "n" : 1 , "c" : "Incrementar el numero de turistas nacionales y extranjeros."},
{"u" : "140000", "o" : "1366" , "t" : "m", "n" : 1 , "c" : "Nuevo Mercado Municipal de Chancay."},
{"u" : "140000", "o" : "1366" , "t" : "m", "n" : 1 , "c" : "Garantizar el empleo permanente al pescador artesanal."},

{"u" : "140000", "o" : "1366" , "t" : "s", "n" : 2 , "c" : "Desarrollar un Plan Integral para la solucion definitiva en la gestion de residuos solidos desde el recojo hasta la construccion de un relleno sanitario, utilizando tecnicas de segregacion en la fuente, reciclaje, compostaje e industrializacion."},
{"u" : "140000", "o" : "1366" , "t" : "s", "n" : 2 , "c" : "Construccion de planta de tratamiento de aguas residuales con la intervencion de la Cooperacion Tecnica Internacional."},
{"u" : "140000", "o" : "1366" , "t" : "s", "n" : 2 , "c" : "Construccion de la entrada a Chancay con un paso a desnivel, desde la Panamericana Norte con la Calle Benjamin Vizquerra a la altura del Colegio Salazar Bondi."},
{"u" : "140000", "o" : "1366" , "t" : "m", "n" : 2 , "c" : "Relleno Sanitario de Residuos Solidos aprobado por DIGESA y con certificacion internacional."},
{"u" : "140000", "o" : "1366" , "t" : "m", "n" : 2 , "c" : "Descontaminar la bahia de Chancay."},
{"u" : "140000", "o" : "1366" , "t" : "m", "n" : 2 , "c" : "Adecuado ingreso y salida vial a la ciudad de Chancay."},

{"u" : "140000", "o" : "1366" , "t" : "s", "n" : 3 , "c" : "Buscar alianzas estrategicas con el sector publico y privado, gestar vinculos con la cooperacion internacional, para implementar un puesto policial o comisaria en Peralvillo."},
{"u" : "140000", "o" : "1366" , "t" : "s", "n" : 3 , "c" : "Construccion de puestos de auxilios rapidos en Chancayllo, Pampa Libre, Candelaria, 28 de Julio y Cerro La Culebra."},
{"u" : "140000", "o" : "1366" , "t" : "s", "n" : 3 , "c" : "Implementar mecanismos compensatorios a la participacion ciudadania."},
{"u" : "140000", "o" : "1366" , "t" : "m", "n" : 3 , "c" : "Reduccion de la delincuencia e inseguridad."},
{"u" : "140000", "o" : "1366" , "t" : "m", "n" : 3 , "c" : "Mejoramiento de la Seguridad Ciudadana."},
{"u" : "140000", "o" : "1366" , "t" : "m", "n" : 3 , "c" : "Mejoramiento de la Seguridad Ciudadana."},


{"u" : "140000", "o" : "181" , "t" : "s", "n" : 0 , "c" : "Liderazgo politico de Presidente Regional en Sistema Regional Seguridad Ciudadana Relacion estrategica con instituciones PNP, MP, PJ Propiciar dinamismo de los comites de seguridad ciudadana Politicas de prevencion con participacion de sector privado Uso tecnologias de informacion y videovigilancia"},
{"u" : "140000", "o" : "181" , "t" : "s", "n" : 0 , "c" : "Proyecto Educativo Regional Modernizacion institucional del sector educativo Descentralizacion educativa a mediano plazo Mayor presupuesto del gobierno regional cada ano en este rubro Concursos y ferias de ciencia y tecnologia y excelencia Concursos de excelencia para incentivar competencia escolar"},
{"u" : "140000", "o" : "181" , "t" : "s", "n" : 0 , "c" : "Mejoramiento del Sistema Regional Descentralizado de Salud y ejecucion de los planes de desarrollo y vigilancia de la salud publica Elevar niveles de proteccion, apoyo y promocion de la familia, promover la paternidad y maternidad responsables, erradicar la violencia familiar y el trabajo infantil."},
{"u" : "140000", "o" : "181" , "t" : "m", "n" : 0 , "c" : "Reducir accion de delincuencia, crimen organizado y principales indicadores de inseguridad. Prevencion de inseguridad con politicas publicas en educacion, familia y juventud. Red de participacion ciudadana en seguridad organizada y efectiva. Creacion Programa Regional de Rondas Campesinas y Urbanas"},
{"u" : "140000", "o" : "181" , "t" : "m", "n" : 0 , "c" : "Acceso universal a educacion inicial y primaria el 2018 Analfabetismo a 0% al 2018 Programa Mejora de Calidad Educativa 2015-2018 Modernizacion de gestion institucional y pedagogica en UGEL e II.EE. Mejora de infraestructura educativa Programa Especial a Ninos Geniales Programa El Profe Cibernetico"},
{"u" : "140000", "o" : "181" , "t" : "m", "n" : 0 , "c" : "Disminucion de la desnutricion cronica al 10% al 2018 Acceso al agua potable del 85% de la poblacion total y de alcantarillado al 70% (son las metas nacionales al 2021) Programas de prevencion enfermedades cronicas y degenerativas, reduccion de malnutricion y morbimortalidad Programas de Guarderias"},

{"u" : "140000", "o" : "181" , "t" : "s", "n" : 1 , "c" : "Plan de desarrollo economico q mejore la infraestructura productiva con orientacion a agro exportacion Fortalecer gestion empresarial de organizaciones de productores e integracion con enfoque de cuenca Reorganizacion de la Direccion Regional de Agricultura para enfatizar su rol promotor y rector."},
{"u" : "140000", "o" : "181" , "t" : "s", "n" : 1 , "c" : "Desarrollar productos y destinos turisticos que genere una oferta competitiva y sostenible en todas las provincias de Region Lima Promover y fortalecer las capacidades institucionales y humanas para impulsar la competitividad Preservar y poner en valor recursos turisticos, medio ambiente y cultura"},
{"u" : "140000", "o" : "181" , "t" : "s", "n" : 1 , "c" : "Promocion intensiva de inversion privada en las diversas actividades economicas Cobertura total del servicio de energia electrica en toda la region garantizando el acceso a la energia en cada hogar y pyme Capacitacion, acceso financiero, comercializacion y competitividad a pymes de la region."},
{"u" : "140000", "o" : "181" , "t" : "m", "n" : 1 , "c" : "Programa de prevencion agricola con defensas riberenas, encauzamiento de rios y mantenimiento y rehabilitacion de infraestructura de riego Creacion de Parques Agro-Industriales en Canete, Huaral, Huaura y Barranca que promuevan la integracion y articulacion vertical Desarrollo de oferta exportable."},
{"u" : "140000", "o" : "181" , "t" : "m", "n" : 1 , "c" : "Caral sera recurso turistico bandera de la region Elevar flujo de turistas con campanas permanentes de promocion, mercadeo nacional e internacional, diversidad de oferta y mejora de los servicios turisticos Fortalecer los servicios turisticos, el turismo de aventura, ecoturismo, turismo de descanso"},
{"u" : "140000", "o" : "181" , "t" : "m", "n" : 1 , "c" : "Programa de promocion de la industria pesquera con regulacion y control de la extraccion, fiscalizacion de contaminacion, y respeto de las normas sanitarias Implementacion de mercados mayoristas en zonas norte y sur de region Programa apoyo a las pymes en compras estatales y clusters."},

{"u" : "140000", "o" : "181" , "t" : "s", "n" : 2 , "c" : "Mejorar sustancialmente superficie de rodadura de la red vial, especialmente las trochas carrozables y las vias sin afirmar, preferentemente en la sierra Lograr la plena integracion vial del departamento de Lima permitiendo el libre y facil acceso de personas y bienes posibilitando el desarrollo."},
{"u" : "140000", "o" : "181" , "t" : "s", "n" : 2 , "c" : "Plan Regional de Gestion ambiental con programa de monitoreo ambiental Avances en aplicacion de energias limpias Elaborar y ejecutar planes de ordenamiento en principales provincias Planes de capacitacion ambiental a poblacion para elevar conciencia de defensa de la naturaleza y calidad de vida"},
{"u" : "140000", "o" : "181" , "t" : "s", "n" : 2 , "c" : "Plan Regional de Ordenamiento Territorial que oriente hacia red de sistemas urbanos con articulacion de los centros poblados en cada provincia. Plan de desarrollo de las localidades afectadas x conflictos. Sistema de coordinacion gubernamental x cuenca en Huaura, Barranca, Huaral y Canete."},
{"u" : "140000", "o" : "181" , "t" : "m", "n" : 2 , "c" : "Llegar al 2018 con el 50 % de la red vial regional debidamente asfaltada (casi 770 km). Reducir el nivel de vias de trocha Aumentar considerablemente el acceso a Internet y telefonia en toda la region, especialmente en las provincias de sierra Iniciar la construccion de los grandes proyectos."},
{"u" : "140000", "o" : "181" , "t" : "m", "n" : 2 , "c" : "Mejora de servicios de saneamiento en toda la region, potabilizando el agua de consumo, y ampliando el servicio de desagüe, en coordinacion con municipalidades Construccion de sistemas de tratamiento de aguas servidas en cuatro provincias costeras Programa de mejora de gestion de residuos solidos."},
{"u" : "140000", "o" : "181" , "t" : "m", "n" : 2 , "c" : "Programa de formalizacion de propiedad al 95% en la region Aplicar politica de frontera viva en norte y sur de la region y plan de desarrollo de Concon Topara como limite con la region Ica Desarrollo del espacio urbano en la frontera de Lima Metropolitana con Huarochiri: San Antonio y Jicamarca."},

{"u" : "140000", "o" : "181" , "t" : "s", "n" : 3 , "c" : "Modernizar la gestion regional mejorando calidad del servicio a la ciudadania, cohesionando el nivel de mando ejecutivo, agilizando procesos internos, integrando al personal en la vision, mision y objetivos institucionales, con sistemas de gestion estrategica y rendicion de cuentas a la poblacion."},
{"u" : "140000", "o" : "181" , "t" : "s", "n" : 3 , "c" : "Lucha contra la corrupcion en gestion regional y mejora de mecanismos de fiscalizacion y control Mayor transparencia y acceso a la informacion publica en el GORELI y en los gobiernos locales de la region. Desarrollo de capacidades en el servicio civil para propiciar probidad reduciendo la corrupcion"},
{"u" : "140000", "o" : "181" , "t" : "s", "n" : 3 , "c" : "Establecer y respetar la sede actual del gobierno regional con una subsede para la parte sur de la region Profundizar el proceso de descentralizacion regional en todos ambitos que establece la ley y adecuar la estructura regional a las nuevas funciones y competencias logradas."},
{"u" : "140000", "o" : "181" , "t" : "m", "n" : 3 , "c" : "Compromiso y ejercicio del Presidente Regional de un liderazgo a tiempo completo como gobernante Modernizar y actualizar la organizacion y funcionamiento del gobierno regional con gestion por resultados, con una gerencia regional eficiente, descentralizadora y transparente en el uso de los recursos"},
{"u" : "140000", "o" : "181" , "t" : "m", "n" : 3 , "c" : "Generacion de iniciativas concretas de lucha contra la corrupcion Propiciar y reconocer las mejores practicas gubernamentales en materia de probidad y transparencia Rendiciones de cuentas frente a la ciudadania mejorando mecanismos de participacion Mejora constante de los portales electronicos."},
{"u" : "140000", "o" : "181" , "t" : "m", "n" : 3 , "c" : "Programa de descentralizacion regional con medicion de avance de objetivos sectoriales Constituir el Comite Intergubernamental de la Region Lima conformada por la PCM y representantes de los sectores, el Gobierno Regional de Lima, los alcaldes provinciales y representantes de alcaldes distritales."},


{"u" : "140000", "o" : "4" , "t" : "s", "n" : 0 , "c" : "1. desarrollar programa educativo del adulto mayor"},
{"u" : "140000", "o" : "4" , "t" : "s", "n" : 0 , "c" : "Programa de seguridad alimentaria"},
{"u" : "140000", "o" : "4" , "t" : "s", "n" : 0 , "c" : "Programa de capacitacion de docentes."},
{"u" : "140000", "o" : "4" , "t" : "m", "n" : 0 , "c" : "1. Region Lima libre de Analfabetismo"},
{"u" : "140000", "o" : "4" , "t" : "m", "n" : 0 , "c" : "Reducir la desnutricion infantil de 12% a 8%."},
{"u" : "140000", "o" : "4" , "t" : "m", "n" : 0 , "c" : "Reducir el problema de aprendizaje de matematica de 41.1% a 20%"},

{"u" : "140000", "o" : "4" , "t" : "s", "n" : 1 , "c" : "Capacitar a 3500 jovenes en 2 anos"},
{"u" : "140000", "o" : "4" , "t" : "s", "n" : 1 , "c" : "Construccion de un Mega puerto en Huacho y la construccion de un tren Bala Huacho(Peru) – Rio de Janeiro(Brasil)."},
{"u" : "140000", "o" : "4" , "t" : "m", "n" : 1 , "c" : "Los productores contraten el 80% de los tecnicos capacitados."},
{"u" : "140000", "o" : "4" , "t" : "m", "n" : 1 , "c" : "Lograr financiamiento de BIF- CAF, con la finalidad de una integracion territorial y economica."},

{"u" : "140000", "o" : "4" , "t" : "s", "n" : 2 , "c" : "Priorizar proyectos de asfaltado y afirmamiento de carretera"},
{"u" : "140000", "o" : "4" , "t" : "s", "n" : 2 , "c" : "Planes de prevencion de colegios y sociedad civil"},
{"u" : "140000", "o" : "4" , "t" : "m", "n" : 2 , "c" : ". 100% de asfaltado y afirmamiento de carretera"},
{"u" : "140000", "o" : "4" , "t" : "m", "n" : 2 , "c" : "Proteccion y limpieza de las 11 cuencas de Region Lima."},

{"u" : "140000", "o" : "4" , "t" : "s", "n" : 3 , "c" : ". Priorizar el gasto en modernizar las casas comunales a nivel local provincial."},
{"u" : "140000", "o" : "4" , "t" : "s", "n" : 3 , "c" : "Contratar a especialistas en las areas de gobierno."},
{"u" : "140000", "o" : "4" , "t" : "s", "n" : 3 , "c" : "Contratar a profesionales y ofrecer incentivos por metas a corto plazo."},
{"u" : "140000", "o" : "4" , "t" : "m", "n" : 3 , "c" : "Adecuados locales para capacitar a lideres en Comunidades, Centro Poblado, Distrito, y Provincias."},
{"u" : "140000", "o" : "4" , "t" : "m", "n" : 3 , "c" : "Gobierno regional eficiente y altamente tecnificado."},
{"u" : "140000", "o" : "4" , "t" : "m", "n" : 3 , "c" : "Gobierno regional eficiente y altamente tecnificado."},


{"u" : "140000", "o" : "5" , "t" : "s", "n" : 0 , "c" : "Re formulacion y ejecucion del Plan Educativo Regional (PER)."},
{"u" : "140000", "o" : "5" , "t" : "s", "n" : 0 , "c" : "Lucha frontal contra la corrupcion y la inseguridad ciudadana en todos los niveles del Estado"},
{"u" : "140000", "o" : "5" , "t" : "s", "n" : 0 , "c" : "Incorporar al 2018 a familias en situacion de riesgo y de extrema pobreza a todos los programas sociales del gobierno"},
{"u" : "140000", "o" : "5" , "t" : "m", "n" : 0 , "c" : "Mejora de la educacion en comprension lectora y racionamiento logico matematico en un 50% de los ninos y jovenes de la region Lima"},
{"u" : "140000", "o" : "5" , "t" : "m", "n" : 0 , "c" : "Convertir a la region Lima en el ano 2018 en un territorio con cero"},
{"u" : "140000", "o" : "5" , "t" : "m", "n" : 0 , "c" : "Reducir la indigencia y la pobreza en un 50% en el periodo 2015-2018"},

{"u" : "140000", "o" : "5" , "t" : "s", "n" : 1 , "c" : "La competitividad que propugnamos para las nueve pro-vincias no se reduce a la busqueda de crecimiento economico, sino se orienta al desa-rrollo de cada uno de los ejes estrategicos regional"},
{"u" : "140000", "o" : "5" , "t" : "s", "n" : 1 , "c" : "Promover cursos, seminarios, conferencias y coaching para mejorar las condiciones de empleabilidad a personas de baja calificacion laboral"},
{"u" : "140000", "o" : "5" , "t" : "s", "n" : 1 , "c" : "Promocion y creacion del Banco Regional para la generacion de empleo de micro, pequenos y medianos empresarios con creditos blandos"},
{"u" : "140000", "o" : "5" , "t" : "m", "n" : 1 , "c" : "Incrementar la productibilidad con margenes de utilidad en un 50% en los sectores productivos de la region Lima"},
{"u" : "140000", "o" : "5" , "t" : "m", "n" : 1 , "c" : "La meta es contar con un programa de desarrollo de capacidades internas y ex-ternas para lograr competitividad profesional y tecnica"},
{"u" : "140000", "o" : "5" , "t" : "m", "n" : 1 , "c" : "La meta es lograr una entidad financiera (Banco Regional) de fomento pro-ductivo para lograr colocar 100 millones de soles de la CTI."},

{"u" : "140000", "o" : "5" , "t" : "s", "n" : 2 , "c" : "Proyecto de tratamiento de residuos solidos con enfoque de territorio para las nueve provincias con planes integrales de mancomunidad distrital, provincial y regional"},
{"u" : "140000", "o" : "5" , "t" : "s", "n" : 2 , "c" : "Contribuir a la conservacion y uso racional del recurso hidrico con enfoque de manejo y gestion de cuenca con el consejo de cuencas de acuerdo a ley y su reglamento"},
{"u" : "140000", "o" : "5" , "t" : "s", "n" : 2 , "c" : "Proyectos para poner en marcha agua para todas las familias de la region Lima y superar la brecha"},
{"u" : "140000", "o" : "5" , "t" : "m", "n" : 2 , "c" : "La meta es cofinanciar los proyectos de residuos solidos en la cada cuenca de la region Lima"},
{"u" : "140000", "o" : "5" , "t" : "m", "n" : 2 , "c" : "partir de la propia ley de la naturaleza con proyectos integrales por cuencas hidrograficas"},
{"u" : "140000", "o" : "5" , "t" : "m", "n" : 2 , "c" : "En el ano 2018 todas las poblaciones de la region Lima contaran con agua limpia, sana e inocua que no afecte la salud de las familias de la region Lima"},

{"u" : "140000", "o" : "5" , "t" : "s", "n" : 3 , "c" : "Foros y Conferencias de alto nivel en forma mensual sobre diferentes temas de actualidad entre la Universi-dad, GORE Lima y empresas privadas"},
{"u" : "140000", "o" : "5" , "t" : "s", "n" : 3 , "c" : "Constituir Redes de Cooperacion Local de jovenes en todos los distritos y provincias de la region con cen-tros de informacion"},
{"u" : "140000", "o" : "5" , "t" : "s", "n" : 3 , "c" : "Constitucion de Registro de consultores especialistas para desarrollar asistencia tecnica especializada a la micro, pequena y mediana empresa de la region"},
{"u" : "140000", "o" : "5" , "t" : "m", "n" : 3 , "c" : "La meta es desarrollar un evento de impacto regional por mes en la region con expositores nacionales e internaciones con convenio con las universidades publicas y privadas"},
{"u" : "140000", "o" : "5" , "t" : "m", "n" : 3 , "c" : "La meta es formar Redes de Cooperacion Local a nivel distrital y provincial para lograr diagnosticos y com-promisos sociales y politicos en el desarrollo social y economico"},
{"u" : "140000", "o" : "5" , "t" : "m", "n" : 3 , "c" : "La region contara con un registro de consultores especialistas para dar apoyo tecnico a las empresas de la region con financiamiento compartido de recursos publicos y privados"},


{"u" : "140000", "o" : "47" , "t" : "s", "n" : 0 , "c" : "ARTICULAR E IMPLEMENTAR EL SISTEMA DE SALUD E INTERCOMUNICARLOS A TRAVES DE UN SISTEMA DE COMUNICACIONES Y POR EQUIPOS DE PREVENCIoN Y DE CURATIVOS ENTRE TODOS LOS CENTROS DE SALUD DE LA REGIoN; Y DESCENTRALIZAR A LOS MEDICOS Y ENFERMERAS EN TODAS LAS ZONAS TERRITORIALES Y POR PISOS GEOGRAFICOS."},
{"u" : "140000", "o" : "47" , "t" : "s", "n" : 0 , "c" : "IMPLEMENTAR EL SEGURO POPULAR DE SALUD, SPS, COMO COMPLEMENTO DEL SISTEMA INTEGRAL DE SALUD, PARA TODOS LOS COMUNICADORES SOCIALES, AMAS DE CASA, MOTOTAXISTAS, TAXISTAS, CAMPESINOS, AGRICULTORES Y PESCADORES ARTESANALES QUE NO CUENTEN CON SEGURO DE SALUD."},
{"u" : "140000", "o" : "47" , "t" : "s", "n" : 0 , "c" : "IMPLEMENTACIoN DE UN SISTEMA DE CIENCIA Y TECNOLOGIA REGIONAL, CONSTRUCCIoN DE COLEGIOS MAYORES REGIONALES, DE VIVIENDAS DE INTERES SOCIAL, DE INFRAESTRCTURAS DE AGUA POTABLE Y DESAGUE. CREAR EL PROGRAMA LABORAL JOVENES A LA OBRA."},
{"u" : "140000", "o" : "47" , "t" : "m", "n" : 0 , "c" : "QUE EL 80% DE LOS CENTROS DE SALUD DE LOS 128 DISTRITOS ESTEN SISTEMATIZADOS Y COMUNICADOS, ASI COMO CADA CENTRO DE SALUD CUENTE MINIMO CON UN MEDICO Y UNA ENFERMERA."},
{"u" : "140000", "o" : "47" , "t" : "m", "n" : 0 , "c" : "QUE CIEN MIL PERSONAS CUENTEN CON SU SEGURO DE SALUD."},
{"u" : "140000", "o" : "47" , "t" : "m", "n" : 0 , "c" : "CONSTRUCCIoN E IMPLEMENTACION DE UN SISTEMA DE CIENCIA Y TECNOLOGIA CON CINCO COLEGIOS MAYORES REGIONALES. CONSTRUCCIoN DE VEINTE MIL VIVIENDAS DE INTERES SOCIAL. DOTACIoN DE AGUA POTABLE A DOSCIENTOS MIL PERSONAS. CIEN MIL NUEVOS PUESTOS DE TRABAJO DIRECTOS E INDIRECTOS."},

{"u" : "140000", "o" : "47" , "t" : "s", "n" : 1 , "c" : "CREACIoN DE LAS UNIDADES REGIONALES DE ASISTENCIA, TRANSFERENCIA Y AJUSTE TECNICA AGROPECUARIAS, URATAS; REFLOTAMIENTAMIENTO DE PUERTOS REGIONALES Y DE COMERCIALIZACION; PRIORIDAD DEL SECTOR CONSTRUCCIoN EN EL SECTOR AGRARIO Y DE VIVIENDA; INSTALACION DE CINCO EJES ECONoMICOS FINANCIEROS REGIONALES."},
{"u" : "140000", "o" : "47" , "t" : "s", "n" : 1 , "c" : "ESTABLECIMIENTO DE UN CONSEJO ECONoMICO Y FINANCIERO CON PARTICIPACIoN DEL SECTOR EMPRESARIAL, TRABAJADORES Y ESTADO, A FIN DE DISENAR POLITICAS DE GESTIoN DE INVERSION INTERNACIONAL PARA MEGAPROYECTOS DE IMPACTO REGIONAL."},
{"u" : "140000", "o" : "47" , "t" : "s", "n" : 1 , "c" : "APROBACION DE UNA POLITICA REGIONAL DE TRANSPORTES Y DE COMUNICACIONES PARA UNIR LOS 128 DISTRITOS, Y GESTIONAR CINCO MEGAPROYECTOS EN ESTE SECTOR."},
{"u" : "140000", "o" : "47" , "t" : "m", "n" : 1 , "c" : "NUEVE URATAS FUNCIONANDO EN NUEVE PROVINCIAS. DOS PUERTOS EN PLENA OPERACIoN PARA EL SECTOR MINERO Y AGROPECUARIO. CUATRO MEGAMERCADOS AGROPECUARIOS. CINCUENTA MIL NUEVAS HECTAREAS AGROPECUARIAS HABILITADAS COMO MINIMO. CREACION DE UN ENTE REGIONAL FINANCIERO."},
{"u" : "140000", "o" : "47" , "t" : "m", "n" : 1 , "c" : "EJECUCIoN DE DIEZ MEGAPROYECTOS MINEROS, ENERGETICOS Y PESQUEROS. DOS EN EL EJE ECONoMICO CANETE YAUYOS, DOS EN EL EJE ECONoMICO HUROCHIRI. DOS EN EL EJE ECONoMICO HUARA- CANTA. DOS EN EL EJE ECONoMICO HUAURA-OYON Y DOS EN EL EJE ECONoMICO BARRANCA-CAJATAMBO."},
{"u" : "140000", "o" : "47" , "t" : "m", "n" : 1 , "c" : "UNO DE TRANSPORTES DE NIVEL REGIONAL. DOS MEGAPROYECTOS DE TRANSPORTES INTERPROVINCIAL. DOS MEGAPROYECTOS DE COMUNICACIONES DE NIVEL REGIONAL."},

{"u" : "140000", "o" : "47" , "t" : "s", "n" : 2 , "c" : "GESTIoN DE RECURSOS ECONoMICOS-FINANCIEROS NACIONALES E INTERNACIONALES PARA LA RECONVERSIoN DE LOS EQUIPOS DE PRODUCCIoN DE LAS EMPRESAS CONTAMINANTES, EN EL ESQUEMA ALIANZA PUBLICO-PRIVADA."},
{"u" : "140000", "o" : "47" , "t" : "s", "n" : 2 , "c" : "MONITOREO Y SEGUIMIENTO AMBIENTAL A TRAVES DE LA CREACIoN DEL INSTITUTO REGIONAL METEOROLIGICO-AMBIENTAL DE LAS DIEZ CUENCAS HIDROGRAFICAS DE LA REGIoN,, PARA EL QUE SE ESTABLECERA SUB ESTACIONES PROVINCIALES."},
{"u" : "140000", "o" : "47" , "t" : "s", "n" : 2 , "c" : "GESTIoN DE RECURSOS ECONoMICO-FINANCIEROS INTERNACIONALES CON PARTICIPACIoN DE LOS GREMIOS EMPRESARIALES PARA LA RECONVERSION DE LOS EQUIPOS Y MAQUINARIAS CONTAMINANTES Y LA ERRADICACIoN DE LOS PROBLEMAS ANTERIORES."},
{"u" : "140000", "o" : "47" , "t" : "m", "n" : 2 , "c" : "QUE TODAS LAS INDUSTRIAS Y EMPRESAS MINERAS, ELECTRICAS, ENERGETICIAS, APROPECUARIAS, PESQUERAS Y PETROLERAS HAYAN SIDO PARTICIPES DE LA GESTION DE RECURSOS ECONoMICOS-FINANCIEROS PARA LA RECCONVERSIoN DE SUS EQUIPOS DE PRODUCCIoN."},
{"u" : "140000", "o" : "47" , "t" : "m", "n" : 2 , "c" : "FUNCIONAMIENTO DE UN INSTITUTO REGIONAL METEREOLoGICO-AMBIENTAL Y DE 27 SUB ESTACIONES PROVINCIALES."},
{"u" : "140000", "o" : "47" , "t" : "m", "n" : 2 , "c" : "CAMPOS AGROPECUARIOS CON MEJOR MANEJO DE AGROQUIMICOS; MAR, RIOS, SUELOS Y CIELOS MENOS CONTAMINADOS."},

{"u" : "140000", "o" : "47" , "t" : "s", "n" : 3 , "c" : "RESTRUCTURACIoN INSTITUCIONAL E IMPLEMENTACIoN DE UNA REINGENIERIA ORIENTADA AL DESARROLLO, A LA SEGURIDAD CIUDADANA Y A LA LUCHA CONTRA LA CORRUPCION,"},
{"u" : "140000", "o" : "47" , "t" : "s", "n" : 3 , "c" : "CONSTRUCCIoN DE UNA NUEVA IDENTIDAD EMPEZANDO POR UNA INICIATIVA LEGISLATIVA PARA EL CAMBIO DE LA DENOMINACIoN DE REGIoN DE LIMA POR LA DE REGION BOLIVAR, Y FORTALECER EL CAPITAL HUMANO EXISTENTE CON LA CONVOCATORIA DE MAS RECURSOS HUMANOS ESPECIALIZADDOS."},
{"u" : "140000", "o" : "47" , "t" : "s", "n" : 3 , "c" : "ELEVAR EL PRESUPUESTO INSTITUCIONAL ANUALMENTE HASTA ALCANZAR EL MONTO DE DOS MIL MILLONES ANUALES."},
{"u" : "140000", "o" : "47" , "t" : "m", "n" : 3 , "c" : "INSTITUCIoN DINAMICA, RAPIDA Y DE BUEN SERVICIO AL CIUDADANO Y LIDER NACIONAL EN LA LUCHA CONTRA LA CORRUPCIoN Y LA INSEGURIDAD CIUDADANA. ASDEMAS DE INCORPORAR AL EMPRESARIADO EN LA SOLUCIoN DE PROBLEMAS SOCIALES Y EN LA GESTIoN DE LA INVERSIoN NACIONAL E INTERNACIONAL."},
{"u" : "140000", "o" : "47" , "t" : "m", "n" : 3 , "c" : "NACIMIENTO DE LA NUEVA REGIoN BOLIVAR"},
{"u" : "140000", "o" : "47" , "t" : "m", "n" : 3 , "c" : "QUE LA NUEVA REGIoN BOLIVAR CUENTE CON DOS MIL MILLONES ANUALES."},


{"u" : "140000", "o" : "2259" , "t" : "s", "n" : 0 , "c" : "-	Garantizar y ampliar la cobertura del acceso equitativo a los servicios de salud, de la poblacion pobre y pobre extrema, a traves del regimen subsidiado y no subsidiado del Seguro Integral de Salud y otros mecanismos de aseguramiento."},
{"u" : "140000", "o" : "2259" , "t" : "m", "n" : 0 , "c" : "Promover mecanismos de coordinacion de los establecimientos de salud con los gobiernos locales y fortalecer los espacios de concertacion intrasectorial, intersectorial e interinstitucional para el abordaje de prioridades locales."},

{"u" : "140000", "o" : "2259" , "t" : "s", "n" : 1 , "c" : "Desarrollar cadenas productivas adecuadamente priorizadas con personal suficiente y adecuadamente capacitado para la actividad exportadora."},
{"u" : "140000", "o" : "2259" , "t" : "m", "n" : 1 , "c" : "Explorar nuevas oportunidades demarcados externos que permitan el acceso en terminos competitivos y rentables de los productos naturales o procesados de la region."},

{"u" : "140000", "o" : "2259" , "t" : "s", "n" : 2 , "c" : "Apoyar y coordinar con las Municipalidades Provinciales y Distritales la formulacion de Planes de Desarrollo Urbano, que contribuyan a mejorar y ampliar los servicios de saneamiento basico en zonas urbano-marginales y rurales."},
{"u" : "140000", "o" : "2259" , "t" : "m", "n" : 2 , "c" : "Implementacion de programas de riego tecnificado para cultivos en zonas con potencial de cultivo permanente y agro exportador."},

{"u" : "140000", "o" : "2259" , "t" : "s", "n" : 3 , "c" : "Efectuar acciones administrativas enmarcadas dentro de una politica de austeridad y transparencia en los gastos que permita un manejo eficiente y eficaz de limitados recursos de la Region."},
{"u" : "140000", "o" : "2259" , "t" : "m", "n" : 3 , "c" : "Se cuenta con recursos financieros y tecnicos para desarrollar proyectos."},



{"u" : "120000", "o" : "2191" , "t" : "s", "n" : 0 , "c" : "1.	Impulsar la generacion de la data de informacion georeferenciada de las lineas de base socioeconomicos de la Region."},
{"u" : "120000", "o" : "2191" , "t" : "m", "n" : 0 , "c" : "1.	Articular y priorizar la gestion con el Sistema de los gobiernos subnacionales de la Region y el Organo de Gestion, Monitorero y Proinversion Regional 2. Financiacion estrategica del desarrollo social con el sistema financiero internacional."},

{"u" : "120000", "o" : "2191" , "t" : "s", "n" : 1 , "c" : "1.	Gestionar las fuentes financieras internacionales para el sector economico, industrial, turistico y de servicios."},
{"u" : "120000", "o" : "2191" , "t" : "m", "n" : 1 , "c" : "1.	Difusion de los beneficios y politicas del Sistema Financiero Internacional. 2. Registro del sector economico, industrial y de servicios a involucrarse en libertad al credito internacional"},

{"u" : "120000", "o" : "2191" , "t" : "s", "n" : 2 , "c" : "1.	Integrar la diversidad biologica y la ordenacion de los ecosistemas en las actividades de planificacion del desarrollo y del sector de produccion;"},
{"u" : "120000", "o" : "2191" , "t" : "m", "n" : 2 , "c" : "1.1.	Iniciar el Plan de Zonificacion Economica y Ecologica (ZEE) 1.2.	Inversion Estrategica Priorizada en cuencas hidrograficas. 1.3.	Elaboracion y ejecucion de Proyectos Productivos para el sector privado via credito estrategico internacional 1.4.	Desarrollo de la mineria responsable."},

{"u" : "120000", "o" : "2191" , "t" : "s", "n" : 3 , "c" : "1.	Modificar el Modelo de Gobernabilidad"},
{"u" : "120000", "o" : "2191" , "t" : "m", "n" : 3 , "c" : "1.	La Agenda Regional Sectorial en el corto, mediano y largo plazo lo disenara: 1.1.	El Presidente Regional 1.2.	El Organo Especializado de Promocion, Gestion, Monitoreo y de proinversion"},


{"u" : "120000", "o" : "2160" , "t" : "s", "n" : 0 , "c" : "1.	Acceso universal a servicios basicos de salud de calidad, con enfasis en su promocion y prevencion."},
{"u" : "120000", "o" : "2160" , "t" : "s", "n" : 0 , "c" : "2.	Aplicacion del Plan de Salud concertado."},
{"u" : "120000", "o" : "2160" , "t" : "s", "n" : 0 , "c" : "3.	Promocion de la salud a traves de una politica de seguridad alimentaria y el mejoramiento de los servicios de salud descentralizados (provincias y distritos). 4. Campanas de promocion de la salud. 5.	Asegurar el financiamiento para el Plan de Salud. 6.	Gestion eficiente, honesta y transparente de"},
{"u" : "120000", "o" : "2160" , "t" : "m", "n" : 0 , "c" : "1.	Se procurara llegar a cubrir el 25% de eficiencia."},
{"u" : "120000", "o" : "2160" , "t" : "m", "n" : 0 , "c" : "2.	Reducir al menos al 15% la prevalencia de desnutricion cronica en menores de 5 anos."},
{"u" : "120000", "o" : "2160" , "t" : "m", "n" : 0 , "c" : "3.	Reducir la tasa de mortalidad infantil en dos terceras partes al ano 2015. 4.	El Plan de Salud concertado se aplicara en un 75%."},

{"u" : "120000", "o" : "2160" , "t" : "s", "n" : 1 , "c" : "1.	Promover un nuevo modelo de desarrollo sostenible integrador fomentando la pequena y mediana agricultura, la industria, la pesca, la ganaderia y el turismo. Impulsar y fomentar la agricultura familiar."},
{"u" : "120000", "o" : "2160" , "t" : "s", "n" : 1 , "c" : "2.	Impulso y promocion de la pequena y mediana empresa, como la industria del calzado y otras actividades productivas. 3.	Promover el desarrollo integral de los distritos y pueblos del interior, de acuerdo al Proyecto Regional de Desarrollo. 4.	Promover iniciativas para la descentralizacion fiscal"},
{"u" : "120000", "o" : "2160" , "t" : "s", "n" : 1 , "c" : "5.	Promover iniciativas para poner limites a la concentracion de tierras. 6.	Gestion con participacion de la poblacion para que el Ministerio de Economia y Finanzas asigne el presupuesto necesario y oportuno para la implementacion de los planes concertados existentes. 7. Promover el desarrollo de ec"},
{"u" : "120000", "o" : "2160" , "t" : "m", "n" : 1 , "c" : "1.	En el caso del nuevo modelo economico, se sentaran las bases para dicho cambio estructural. 2.	Se aspira a abarcar al 40% de la pequena y mediana agricultura, promoviendo la asociatividad."},
{"u" : "120000", "o" : "2160" , "t" : "m", "n" : 1 , "c" : "3.	Incrementar en 30% la superficie agricola bajo riego en la sierra y 50% en la costa. 4.	Las economias alternativas llegan a un 20%."},
{"u" : "120000", "o" : "2160" , "t" : "m", "n" : 1 , "c" : "5.	Disminucion de la pobreza a indices menores que el promedio nacional. 6.	Disminucion del empleo y subempleo a indices menores que el promedio nacional. 7.	Las empresas de la region pagaran el integro de sus impuestos y demas obligaciones."},

{"u" : "120000", "o" : "2160" , "t" : "s", "n" : 2 , "c" : "1.	Promover un sistema de transporte multimodal, moderno, eficiente y competitivo promoviendo la integracion territorial con perspectivas de zonas de desarrollo. 2.	Dotar de energia electrica a los principales centros poblados de La Libertad."},
{"u" : "120000", "o" : "2160" , "t" : "s", "n" : 2 , "c" : "3.	Promover la generacion y uso de fuentes renovables de energia. 4.	Ampliar y mejorar los servicios de telecomunicaciones con enfasis en las zonas rurales y urbano – marginales."},
{"u" : "120000", "o" : "2160" , "t" : "s", "n" : 2 , "c" : "10.	Promover con enfoque de cuenca, el uso eficiente y sostenible del recurso hidrico en la region La Libertad. 11. Promover la incorporacion de la gestion del Riesgo y la Adaptacion al cambio climatico en la formulacion y aplicacion de los instrumentos de planificacion."},
{"u" : "120000", "o" : "2160" , "t" : "m", "n" : 2 , "c" : "Las 12 provincias de La Libertad se encuentran interconectadas por medio de carreteras asfaltadas y en buen estado. -	Reduccion de la brecha entre la zona urbana y rural, aumentando el acceso a energia electrica en zonas rurales a 60%"},
{"u" : "120000", "o" : "2160" , "t" : "m", "n" : 2 , "c" : "-	La brecha digital en terminos de acceso a internet se reduce al menos en 20%. -	50% de las cuencas hidrograficas de la region se gestionaran con un plan integral."},
{"u" : "120000", "o" : "2160" , "t" : "m", "n" : 2 , "c" : "-	El 40% de proyectos relacionados con el medio ambiente se articulan al mercado de bonos de carbon o mecanismos similares."},

{"u" : "120000", "o" : "2160" , "t" : "s", "n" : 3 , "c" : "1.	Incentivar y promover el compromiso de las instituciones publicas y privadas para llevar a la practica el Plan Regional de Desarrollo Concertados. 2.	Desarrollar una institucionalidad publica eficiente, transparente, promotora y orientada al usuario."},
{"u" : "120000", "o" : "2160" , "t" : "s", "n" : 3 , "c" : "3.	Promover la participacion democratica y la concertacion en la gestion del desarrollo."},
{"u" : "120000", "o" : "2160" , "t" : "s", "n" : 3 , "c" : "5.	Plan integral para la lucha contra la corrupcion y el narcotrafico con participacion de la ciudadania. 6.	Politica regional anticorrupcion para erradicar este cancer del aparato administrativo del estado y en las empresas privadas. 7.	Campanas intensivas para prevencion de la corrupcion."},
{"u" : "120000", "o" : "2160" , "t" : "m", "n" : 3 , "c" : "-	Entre el 25% y 30% de las instituciones publicas y privadas se comprometen con el Plan concertado de Desarrollo regional. -	El 50% de las instituciones se comprometen con una gestion eficiente, honesta y transparente."},
{"u" : "120000", "o" : "2160" , "t" : "m", "n" : 3 , "c" : "-	El 75% del magisterio regional se compromete con la labor educativa en la formacion de valores. -	El 100% de las licitaciones para obras publicas se hacen con transparencia.."},
{"u" : "120000", "o" : "2160" , "t" : "m", "n" : 3 , "c" : "-	En el cumplimiento de la Ley de Transparencia informativa la Libertad se ubicara entre los 10 primeros. - Existira un sistema de informacion regional confiable articulado a otros sistemas de informacion nacionales y/o internacionales. -	60% de los ciudadanos satisfechos con los servicios que brind"},


{"u" : "120000", "o" : "32" , "t" : "s", "n" : 0 , "c" : "- Incremento de los niveles de Inversion publica regional y la prioridad que el estado y sociedad Peruana otorgan a la lucha contra la pobreza. - Inversion en infraestructura de servicios basicos y viales y fortalecimiento de capacidades en la poblacion."},
{"u" : "120000", "o" : "32" , "t" : "s", "n" : 0 , "c" : "- Mejoramiento de la cobertura del servicio educativo. - Mejora de la calidad educativa. - Gestionar el financiamiento ante el MEF."},
{"u" : "120000", "o" : "32" , "t" : "s", "n" : 0 , "c" : "- Mejoramiento de la atencion de salud en La Libertad. - Disminucion de la mortalidad materna e infantil. - Mejoramiento de la cobertura de servicios de agua y alcantarillado."},
{"u" : "120000", "o" : "32" , "t" : "m", "n" : 0 , "c" : "- Reduccion de la pobreza monetaria en 5%. - Reduccion de la pobreza extrema en 2%."},
{"u" : "120000", "o" : "32" , "t" : "m", "n" : 0 , "c" : "- Construccion de 400 aulas nuevas. - Equipamiento a Instituciones educativas. - Incremento en el nivel de comprension lectora al 40%. - Incremento en el nivel de razonamiento matematico en 25%. - Incremento de 1000 plazas de docentes y 400 plazas de personal auxiliar y de servicios."},
{"u" : "120000", "o" : "32" , "t" : "m", "n" : 0 , "c" : "- Mejorar la Infraestructura y equipamiento en 40 establecimientos de salud y dos institutos de salud especializado. - Implantacion de un laboratorio de referncia regional. - Disminucion de la muerte materna en un 30%. - Construccion de 50 Km. y 15 mil conexiones domiciliarias de agua potable"},

{"u" : "120000", "o" : "32" , "t" : "s", "n" : 1 , "c" : "- Integrar a las capitales provinciales y principales valles, priorizando la inversion en la red vial."},
{"u" : "120000", "o" : "32" , "t" : "s", "n" : 1 , "c" : "- Consolidacion de la infraestructura de servicios al sector productivo, mediante la promocion de la inversion privada y desarrollo de actvidades economicas."},
{"u" : "120000", "o" : "32" , "t" : "s", "n" : 1 , "c" : "- Promocion de la inversion privada mediante el desarrollo de proyectos estrategicos con mecanismos de financiamiento Publico - Privado."},
{"u" : "120000", "o" : "32" , "t" : "m", "n" : 1 , "c" : "- Asfaltado de 250 Kms. en carreteras departamentales. - Afirmado de 500 Kms. en carreteras departamentales. - Construccion de 300 Km de trochas carrozable. - Mantenimiento de 300 Km de carretera."},
{"u" : "120000", "o" : "32" , "t" : "m", "n" : 1 , "c" : "- Apoyar los proyectos municipales de acceso a la electricidad. - Construir 60 Km en canales de riego. - Construir 20 Km. de defensa riberenas."},
{"u" : "120000", "o" : "32" , "t" : "m", "n" : 1 , "c" : "- Ejecutar la III etapa del Proyecto CHAVIMOCHIC. - Impulsar el financiamiento de la II etapa del Proyecto Jequetepeque - Zana. - Gestionar ante MTC la culminacion de la via Huamachuco - Abra de Naranjillo en el Proyecto Salaverry - Juanjui. - Gestiones para el nuevo aeropuerto de Trujillo."},

{"u" : "120000", "o" : "32" , "t" : "s", "n" : 2 , "c" : "- Disminucion de la contaminacion ambiental y preservacion de los recursos naturales. - Conservar la diversidad biologica y los recursos renovables y no renovables de la Region."},
{"u" : "120000", "o" : "32" , "t" : "s", "n" : 2 , "c" : "Promover la conservacion de los recursos naturales y el uso eficiente del recurso hidrico en la Libertad mediante ejecucion de proyectos."},
{"u" : "120000", "o" : "32" , "t" : "m", "n" : 2 , "c" : "- 01 Estudio de zonificacion economica y ecologica aprobado e implementado. - 05 Areas naturales protegidas con planes de manejo."},
{"u" : "120000", "o" : "32" , "t" : "m", "n" : 2 , "c" : "- Ejecucion de proyectos en tres cuencas hidrograficas priorizadas. - Promover a traves del Fondo mi Riego, proyectos para el almacenaje de agua y construccion de canales."},

{"u" : "120000", "o" : "32" , "t" : "s", "n" : 3 , "c" : "Consolidar la modernizacion del Estado, mediante el mejoramiento de los servicios y modernizacion de los sistemas y procesos administrativos."},
{"u" : "120000", "o" : "32" , "t" : "s", "n" : 3 , "c" : "Promocion de la participacion ciudadana en la gestion del desarrollo regional."},
{"u" : "120000", "o" : "32" , "t" : "m", "n" : 3 , "c" : "- Incremento en 50% de la percepcion positiva de los ciudadanos. - Mejoramiento de capacidades a 2,500 trabajadores administrativos y 19 mil docentes. - Construccion y equipamiento de la nueva sede regional. - Descentralizacion de las unidades organicas del Gobierno Regional."},
{"u" : "120000", "o" : "32" , "t" : "m", "n" : 3 , "c" : "- Un portal web y sisetm de informcion entre los cuatro mejores del Pais.- - 150 organizaciones de la sociedad civil, organizadas y capacitadas para la participacion ciudadana."},


{"u" : "120000", "o" : "21" , "t" : "s", "n" : 0 , "c" : "Estructurar una curricula de acuerdo a las necesidades del desarrollo personal y social basado en valores, flexible al integrar las distintas materias al conocimiento de La Region"},
{"u" : "120000", "o" : "21" , "t" : "s", "n" : 0 , "c" : "Gestionar de manera equitativa la atencion integral en salud con calidad y calidez humana, repotenciando las instituciones de salud de toda la region."},
{"u" : "120000", "o" : "21" , "t" : "s", "n" : 0 , "c" : "Organizacion de una fuerza ciudadana consciente y proactiva capaz de institucionalizar la seguridad ciudadana preventiva y proactiva, con participacion vecinal, en funcion de la disminucion de la delincuencia juvenil."},
{"u" : "120000", "o" : "21" , "t" : "m", "n" : 0 , "c" : "Proyecto educativo para la calidad y vigilancia de los servicios educativos. Nueva curricula que incluye el desarrollo de emprendedores para jovenes estudiantes.  Programa de Reactivacion de CEOS. Programa Social Alimentario para la poblacion Escolar. Fortalecimiento de LA DRELL y APAFAS."},
{"u" : "120000", "o" : "21" , "t" : "m", "n" : 0 , "c" : "Construccion de hospitales Nivel I debidamente equipados, implementacion de las instituciones de salud.Asistencia Social para adultos mayores y personas con discapacidad.Proyecto de Inversion Social en conexiones domiciliarias de agua y desagüe, de reciclaje e industrializacion de la basura."},
{"u" : "120000", "o" : "21" , "t" : "m", "n" : 0 , "c" : "Capacitacion e Institucionalidad de Vigilancia Ciudadana.Instalacion de filmadoras y alarmas en sitios estrategicos.Bloquear el ingreso o salida de llamadas de celulares de los penales e implementacion de equipos de rastreo de llamadas.Capacitacion ocupacional y de enlace laboral juvenil."},

{"u" : "120000", "o" : "21" , "t" : "s", "n" : 1 , "c" : "Incrementar la dinamica economica local y comercial de productos agropecuarios y los niveles de produccion, generando empleo digno propiciado por un desarrollo economico sostenible."},
{"u" : "120000", "o" : "21" , "t" : "s", "n" : 1 , "c" : "Fomentar la actividad turistica a nivel regional, con relevancia en la promocion de la gastronomia en toda la Region La Libertad."},
{"u" : "120000", "o" : "21" , "t" : "m", "n" : 1 , "c" : "Proyecto ganadero y frutales.Creacion de nuevas fuentes de trabajo para mano de obra no calificada: Desarrollo de la “Maricultura”,creacion de Escuela para Artesanos de oro y plata.Instalacion del parque industrial con produccion de la madera y pequenas plantas procesadores de nectares y harinas."},
{"u" : "120000", "o" : "21" , "t" : "m", "n" : 1 , "c" : "Promocion de las riquezas turisticas y del material gastronomico de los distintos puntos de la Region. Proyecto de promocion y senalizacion de circuito turistico. Proyecto de promocion de pequenos negocio gastronomicos en redes MYPES."},

{"u" : "120000", "o" : "21" , "t" : "s", "n" : 2 , "c" : "Efectuar el saneamiento de la propiedad de las zonas de residencia urbana y el ordenamiento urbano rural."},
{"u" : "120000", "o" : "21" , "t" : "s", "n" : 2 , "c" : "Incrementar el flujo de transporte con fines comercial y turistico."},
{"u" : "120000", "o" : "21" , "t" : "s", "n" : 2 , "c" : "Reducir la contaminacion ambiental junto con los efectos que causan en la poblacion."},
{"u" : "120000", "o" : "21" , "t" : "m", "n" : 2 , "c" : "Titulacion de la propiedad en zonas de residencia urbana. Plan de ordenamiento territorial urbano rural. Catastro urbano y rural a nivel regional."},
{"u" : "120000", "o" : "21" , "t" : "m", "n" : 2 , "c" : "Infraestructura vial en la sierra.Asfaltado de vias. Infraestructura maritima, portuaria y aereaIniciar un estudio preliminar para el tras- base del Rio Crinejas a la cuenca de Chicama para asegurar el agua en la franja costera y deserticas de nuestra region."},
{"u" : "120000", "o" : "21" , "t" : "m", "n" : 2 , "c" : "Proyecto forestal Estudio de Zonificacion Economica Ecologica. Programa de educacion ambiental y ejecucion de normatividad aplicada. Plan de contingencia, capacitacion, prevencion y defensa civil."},

{"u" : "120000", "o" : "21" , "t" : "s", "n" : 3 , "c" : "Simplificar los procedimientos administrativos y operativos mejorando la calidad de obras a fin de lograr la participacion ciudadana, la concentracion y gobernabilidad."},
{"u" : "120000", "o" : "21" , "t" : "m", "n" : 3 , "c" : "Plan de simplificacion administrativa. Programa de obras duraderas, de calidad Funcionamiento de Consejo de Desarrollo Economico Local. Fondo de inversion de desarrollo economico funcionado"},


{"u" : "120000", "o" : "1264" , "t" : "s", "n" : 0 , "c" : "Drastica reduccion de la red de intermediacion comercial agraria, para incrementar la rentabilidad de la produccion agraria en perspectiva de superar la crisis prolongada de la agricultura regional y la pobreza en el campo"},
{"u" : "120000", "o" : "1264" , "t" : "s", "n" : 0 , "c" : "Politicas de promocion del empleo, nuevos emprendimientos y estrategias eficaces de reduccion de pobreza."},
{"u" : "120000", "o" : "1264" , "t" : "s", "n" : 0 , "c" : "Equilibrio en el destino de los recursos fiscales para la infraestructura vial, educativa y de salud, con los destinados al desarrollo de capacidades y competencias para el desarrollo."},
{"u" : "120000", "o" : "1264" , "t" : "m", "n" : 0 , "c" : "Incremento de la produccion agropecuaria para mejorar la productividad, a partir del acceso de los actores a recursos de tecnologia, financiamiento no convencional, mercadeo directo y formas innovadoras de organizacion"},
{"u" : "120000", "o" : "1264" , "t" : "m", "n" : 0 , "c" : "Incremento de volumenes de exportacion de produccion agricola y pecuaria, por mejor desenvolvimiento de los factores de produccion agroalimentaria"},
{"u" : "120000", "o" : "1264" , "t" : "m", "n" : 0 , "c" : "Intervencion directa del gobierno regional La Libertad, para asegurar una mineria responsable, sostenida y competitiva, propagacion del uso de energias sostenibles y abastecimiento racional de hidrocarburos conforme la demanda"},

{"u" : "120000", "o" : "1264" , "t" : "s", "n" : 1 , "c" : "Rehabilitacion y generacion de sistemas sostenibles de gestion de las fuentes naturales de agua, asegurar accesibilidad de agua dulce a todos los seres humanos que habitan la region y una gestion publica eficiente moderna del agua para consumo humano."},
{"u" : "120000", "o" : "1264" , "t" : "s", "n" : 1 , "c" : "Promocion de las iniciativas de inversion en el campo de la acuicultura y aprovechamiento y gestion sostenible de los recursos del mar"},
{"u" : "120000", "o" : "1264" , "t" : "s", "n" : 1 , "c" : "Intervencion directa del gobierno regional La Libertad, para asegurar una mineria responsable, sostenida y competitiva, propagacion del uso de energias sostenibles y abastecimiento racional de hidrocarburos conforme la demanda"},
{"u" : "120000", "o" : "1264" , "t" : "m", "n" : 1 , "c" : "represamiento natural, almacenamiento con infraestructura tecnica y autosostenible del recurso hidrico"},
{"u" : "120000", "o" : "1264" , "t" : "m", "n" : 1 , "c" : "instalacion de psigranjas con la produccion de especies nativas y exoticas"},
{"u" : "120000", "o" : "1264" , "t" : "m", "n" : 1 , "c" : "meJoramiento de las tecnicas agronomicas, mineras, educativas, viales y de salubridad"},

{"u" : "120000", "o" : "1264" , "t" : "s", "n" : 2 , "c" : "Implementar las redes regionales de iniciativas populares de empresa familiar como estrategia central de eliminacion de la pobreza y de innovacion de los programas sociales en perspectiva de mejores resultados."},
{"u" : "120000", "o" : "1264" , "t" : "s", "n" : 2 , "c" : "Mejoramiento de infraestructura, innovacion organizativa, y ampliacion de cobertura, eficacia y eficiencia de los servicios de salud, con creciente participacion de la sociedad civil y las poblaciones locales, partiendo de experiencia piloto de Redes CLAS asociadas a unidades de atencion quirurgica"},
{"u" : "120000", "o" : "1264" , "t" : "s", "n" : 2 , "c" : "La identificacion y el ejercicio del derecho a la mutua asignacion roles, mediante formulas de negociacion con pares vecinos, para el impulso de proyectos de interes mutuo."},
{"u" : "120000", "o" : "1264" , "t" : "m", "n" : 2 , "c" : "mejoramiento de la infraestructura vial y ordenamiento de ferias de produccion agropecuaria Drastica reduccion de la red de intermediacion comercial agraria, para incrementar la rentabilidad de la produccion agraria en perspectiva de superar la crisis prolongada de la agricultura regional"},
{"u" : "120000", "o" : "1264" , "t" : "m", "n" : 2 , "c" : "implementacion y mejoramiento de la infraestructura de salud. Pleno uso de las competencias legales de la descentralizacion, y generacion del marco legal normativo regional complementario para la profundizacion de la lucha contra los seculares efectos del centralismo, con privilegio en la promocion"},
{"u" : "120000", "o" : "1264" , "t" : "m", "n" : 2 , "c" : "promocion del empleo, nuevos emprendimientos y estrategias eficaces de reduccion de pobreza, No menos del 35% de la red vial regional se encontrara transitable, habilitada y rehabilitada a nivel de afirmado y con un sistema de mantenimiento que garantice su libre y segura transitabilidad"},

{"u" : "120000", "o" : "1264" , "t" : "s", "n" : 3 , "c" : "Estas condiciones devienen en el siguiente enunciado: Se logra Conciencia Activa, al resultado en comportamientos, actitudes, conductas y cultura que alcanzan los ciudadanos por efecto de lograr"},
{"u" : "120000", "o" : "1264" , "t" : "s", "n" : 3 , "c" : "OBJETIVO GENERAL DEL PLAN DE DESARROLLO 2015 – 2018: GENERACION DE RIQUEZA, Aplicar y desarrollar la base conceptual y las estrategias del modelo humanista de economia solidaria, enfocada a desencadenar las potencias naturales al emprendimiento de los varones y mujeres de la Libertad"},
{"u" : "120000", "o" : "1264" , "t" : "s", "n" : 3 , "c" : "Fortalecimiento y modernizacion en eficiencia y competitividad de la inversion empresarial en perspectiva de eliminar el monopolio, los fallos de mercado y la accesibilidad de bienes vitales para la poblacion en desventaja estructural"},
{"u" : "120000", "o" : "1264" , "t" : "m", "n" : 3 , "c" : "a. Un alto y muy objetivo nivel de conocimiento de las propias potencialidades del grupo humano que comparte un territorio comun. b. Un amplio nivel de conocimiento de las potencialidades ambientales, productivas, sociales y culturales. c. Proyectar una elevada valoracion cultural"},
{"u" : "120000", "o" : "1264" , "t" : "m", "n" : 3 , "c" : "Drastica reduccion de la red de intermediacion comercial agraria, para incrementar la rentabilidad de la produccion agraria en perspectiva de superar la crisis prolongada de la agricultura regional y la pobreza en el campo"},
{"u" : "120000", "o" : "1264" , "t" : "m", "n" : 3 , "c" : "Pleno uso de las competencias legales de la descentralizacion, y generacion del marco legal normativo regional complementario para la profundizacion de la lucha contra los seculares efectos del centralismo, con privilegio en la promocion de la produccion, capitalizacion, distribucion y ahorro social"},


{"u" : "120000", "o" : "1257" , "t" : "s", "n" : 0 , "c" : "Impulsar proyectos productivos priorizados que mejoren la situacion socioeconomica, generacion de empleo y la elevacion de la calidad de vida familiar."},
{"u" : "120000", "o" : "1257" , "t" : "s", "n" : 0 , "c" : "Mejorar la comprension lectora y la matematica en el nivel primario y secundario para las proximas evaluaciones censales nacionales e internacionales."},
{"u" : "120000", "o" : "1257" , "t" : "s", "n" : 0 , "c" : "Priorizar una mayor inversion en el area de infraestructura y vivienda para mejorar la cobertura en el servicio de agua potable y alcantarillado"},
{"u" : "120000", "o" : "1257" , "t" : "m", "n" : 0 , "c" : "Disminuir 15% en el Indice de Pobreza Humana (IPH), a partir de transferencia de competencias laborales y empresariales para generar empleo."},
{"u" : "120000", "o" : "1257" , "t" : "m", "n" : 0 , "c" : "-	Analfabetismo 0% en zona rural y urbano marginal. -	Disminuir indice de desercion escolar en educacion primaria y secundaria. -	Construccion de infraestructura"},
{"u" : "120000", "o" : "1257" , "t" : "m", "n" : 0 , "c" : "-	Incrementar el servicio de agua potable al 40% en el ambito rural, y al 85% en el ambito urbano. - Incrementar el servicio de desagüe al 30% en el ambito rural, y al 80% en el ambito urbano"},

{"u" : "120000", "o" : "1257" , "t" : "s", "n" : 1 , "c" : "Priorizar mayor presupuesto regional en el area de infraestructura para atender la ampliacion de la red vial articulada al proceso de desarrollo regional integral."},
{"u" : "120000", "o" : "1257" , "t" : "s", "n" : 1 , "c" : "Promover el consumo de productos agricolas de La Libertad a traves de Ferias Agropecuarias y variadas Campanas Publicitarias.	Difundir la Oferta Exportable Regional"},
{"u" : "120000", "o" : "1257" , "t" : "s", "n" : 1 , "c" : "Promover el turismo, mejorando el desarrollo de la inversion y competitividad, a traves de la calidad y calidez del capital humano que prestan el servicio, incorporando competencias laborales en turismo."},
{"u" : "120000", "o" : "1257" , "t" : "m", "n" : 1 , "c" : "Ejecutar el mantenimiento de carreteras, caminos y puentes en 3 Ejes viales: * Trujillo-Otuzco-Huamachuco-Juanjui. * Otuzco-Usquil - Lucma-Cruce de Cascas. * Viru- Julcan - Santiago de Chuco"},
{"u" : "120000", "o" : "1257" , "t" : "m", "n" : 1 , "c" : "-	Almacenar 190,000 m3 de agua en pequenos reservorios y represas en la sierra libertena. - Implementar 50,000 nuevas Has. irrigadas en la Costa y Sierra de la region. -	Implementar 3,000 Has. atendidas con riego tecnificado en zonas de la sierra."},
{"u" : "120000", "o" : "1257" , "t" : "m", "n" : 1 , "c" : "-	Identificacion de productos turisticos provinciales como parte de una propuesta regional conjunta. - Supervisar un 80% el numero de establecimientos prestadores de servicios turisticos relacionando la certificacion de calidad."},

{"u" : "120000", "o" : "1257" , "t" : "s", "n" : 2 , "c" : "Trabajar el tema de cumplimiento y aplicacion de la normatividad del medio ambiente de acuerdo a leyes y reglamentos nacionales,"},
{"u" : "120000", "o" : "1257" , "t" : "s", "n" : 2 , "c" : "Determinar una agenda regional ambiental que se alinea al Sistema Nacional de Gestion Ambiental y que garantice la representatividad de las provincias y que promueva el uso eficiente y responsable del recurso hidrico."},
{"u" : "120000", "o" : "1257" , "t" : "s", "n" : 2 , "c" : "Mejorar e implementar Normatividad Regional que regulen el uso eficiente y responsable del recurso hidrico como elemento prioritario para el desarrollo regional."},
{"u" : "120000", "o" : "1257" , "t" : "m", "n" : 2 , "c" : "Fortalecimiento del Sistema de Gestion Ambiental Regional en coordinacion de la CAR La Libertad."},
{"u" : "120000", "o" : "1257" , "t" : "m", "n" : 2 , "c" : "-	Garantizar que los sectores regulen y controlen los impactos ambientales de las fuentes de aguas: rios, lagunas. -	Manejo de las areas naturales, dando valor agregado a los recursos naturales."},
{"u" : "120000", "o" : "1257" , "t" : "m", "n" : 2 , "c" : "-	Manejo de cuencas aplicando la Ley de Aguas, Planes de Manejo Integral de cuencas. -	Manejo de la Erosion Costera Incorporando medidas de adaptacion y mitigacion al cambio climatico"},

{"u" : "120000", "o" : "1257" , "t" : "s", "n" : 3 , "c" : "Mejoramiento de infraestructura y equipamiento tecnologico en sedes del gobierno regional. Capacitacion permanente y efectiva a los servidores publicos de la Region."},
{"u" : "120000", "o" : "1257" , "t" : "s", "n" : 3 , "c" : "El gobierno regional propicia y sincera los espacios de participacion ciudadana, comprometiendose en la atencion prioritaria de sus demandas sociales respetando el derecho de representatividad y presencia en la labor conjunta de fiscalizacion."},
{"u" : "120000", "o" : "1257" , "t" : "s", "n" : 3 , "c" : "Generar seguridad en las familias e inversionistas a traves de un trabajo concertado, integral y conjunto que impliquen acciones preventivas y correctivas involucrando a todas las autoridades y sectores del grupo de interes social."},
{"u" : "120000", "o" : "1257" , "t" : "m", "n" : 3 , "c" : "Lograr conformar un grupo humano solido y cohesionado que trabaje con identificacion a nuestra Region y a los intereses del Gobierno Regional."},
{"u" : "120000", "o" : "1257" , "t" : "m", "n" : 3 , "c" : "Cumplir con lo establecido por la norma referida a la participacion y responsabilidad del Consejo de Coordinacion Regional como miembro activo del gobierno regional a traves de su representatividad en las diversas acciones."},
{"u" : "120000", "o" : "1257" , "t" : "m", "n" : 3 , "c" : "Capacitacion e implementacion de todas las rondas campesinas y urbanas de la region, previo inventario tecnico - legal y un diagnostico de necesidades. Crear la Escuela Regional de la Policia de Seguridad Ciudadana como ente autosostenible y rentable"},


{"u" : "120000", "o" : "46" , "t" : "s", "n" : 0 , "c" : "Validar, sistematizar y difundir metodologias pedagogicas exitosas medidas en logros de aprendizajes. Generar una masa critica de docentes con altas calificaciones que permitan llevar adelante las estrategias orientadas al desarrollo educativo. Implementar sist. de medicion de logros de aprendizaje"},
{"u" : "120000", "o" : "46" , "t" : "s", "n" : 0 , "c" : "Ejecutar un programa de inversiones de acceso a agua y desagüe sobre la base de las prioridades del plan de saneamiento para La Libertad En la ejecucion de proyectos de saneamiento, incentivar y priorizar la utilizacion de profesionales, tecnologias y recursos propios de cada zona."},
{"u" : "120000", "o" : "46" , "t" : "m", "n" : 0 , "c" : "Promocion de Metodologias Pedagogicas Exitosas que garanticen aprendizajes de calidad, utiles y pertinentes al desarrollo regional. Promover una gestion participativa y concertada de las estrategias educativas."},
{"u" : "120000", "o" : "46" , "t" : "m", "n" : 0 , "c" : "Garantizar la prestacion equitativa y eficiente de los servicios de agua potable y saneamiento Garantizar servicios de salud de calidad y con calidez."},

{"u" : "120000", "o" : "46" , "t" : "s", "n" : 1 , "c" : "Priorizar mayor presupuesto regional en el area de infraestructura para atender la ampliacion de la red vial articulada al proceso de desarrollo regional integral."},
{"u" : "120000", "o" : "46" , "t" : "s", "n" : 1 , "c" : "Promover el consumo de productos agricolas de La Libertad a traves de Ferias Agropecuarias y variadas Campanas Publicitarias. Difundir la Oferta Exportable Regional."},
{"u" : "120000", "o" : "46" , "t" : "s", "n" : 1 , "c" : "Promover el turismo, mejorando el desarrollo de la inversion y competitividad, a traves de la calidad y calidez del capital humano que presta el servicio, incorporando competencias laborales en turismo."},
{"u" : "120000", "o" : "46" , "t" : "m", "n" : 1 , "c" : "Garantizar la seguridad alimentaria de la poblacion sobre la base del aprovechamiento del potencial agricola de sierra y costa."},
{"u" : "120000", "o" : "46" , "t" : "m", "n" : 1 , "c" : "Institucionalizar el uso de planes de ordenamiento territorial como parte de la gestion de gobierno local y regional."},
{"u" : "120000", "o" : "46" , "t" : "m", "n" : 1 , "c" : "Lograr la identificacion cultural y conciencia turistica local regional. Lograr una gestion participativa y concertada de las estrategias relacionadas al desarrollo del turismo."},

{"u" : "120000", "o" : "46" , "t" : "s", "n" : 2 , "c" : "- Promover la conservacion del medio ambiente y el manejo sostenible e integrado de los recursos naturales y la biodiversidad. - Promover una gestion participativa y concertada de las estrategias relativas a la problematica del medio ambiente"},
{"u" : "120000", "o" : "46" , "t" : "s", "n" : 2 , "c" : "Promover una gestion participativa y concertada de las estrategias relativas a la infraestructura de soporte."},
{"u" : "120000", "o" : "46" , "t" : "m", "n" : 2 , "c" : "Lograr la sostenibilidad del ambiente natural y desarrollar infraestructura de soporte con perspectiva de zonas de desarrollo regional."},
{"u" : "120000", "o" : "46" , "t" : "m", "n" : 2 , "c" : "Lograr la sostenibilidad del ambiente natural y desarrollar infraestructura de soporte con perspectiva de zonas de desarrollo regional."},

{"u" : "120000", "o" : "46" , "t" : "s", "n" : 3 , "c" : "- Practicar y fomentar la gobernabilidad en la region La Libertad. - La gestion participativa y concertada debe guiar la actuacion de las autoridades – funcionarios – empleados regionales y locales."},
{"u" : "120000", "o" : "46" , "t" : "m", "n" : 3 , "c" : "Fortalecer la institucionalidad, la concertacion y participacion ciudadana como medio para alcanzar gobernabilidad."},


{"u" : "120000", "o" : "4" , "t" : "s", "n" : 0 , "c" : "- Diagnostico de cobertura de atencion de la Salud en poblaciones de escasos recursos economicos. - Coordinacion entre autoridades para resolver problemas de ordenamiento de actividades sanitarias."},
{"u" : "120000", "o" : "4" , "t" : "m", "n" : 0 , "c" : "Construccion e implementacion de Hospitales, que permitan una buena atencion con equipos medicos y personal asistencial para mejorar el acceso a la Salud en lugares de escasos recursos economicos y que se requiera atencion especializada"},

{"u" : "120000", "o" : "4" , "t" : "s", "n" : 1 , "c" : "Formulacion de un ordenamiento de zonas comerciales de la region, habilitando espacios para comerciantes y mejorando las vias de acceso, de esta manera promover la lucha contra la pobreza."},
{"u" : "120000", "o" : "4" , "t" : "m", "n" : 1 , "c" : "Ordenamiento y formalizacion del comercio en los distritos, provincias y en toda la region y mejoramiento de las vias de acceso y de comunicacion para abastecer a los mercados nacionales e internacionales."},

{"u" : "120000", "o" : "4" , "t" : "s", "n" : 2 , "c" : "Mejorar la gestion, mediante una planificacion estrategica regional con la adecuada sensibilizacion de los agentes que ocupan el espacio fisico."},
{"u" : "120000", "o" : "4" , "t" : "m", "n" : 2 , "c" : "Evaluaciones de impacto ambiental en forma periodica para mejorar el medio ambiente y su desarrollo del espacio fisico."},

{"u" : "120000", "o" : "4" , "t" : "s", "n" : 3 , "c" : "• Detectar y eliminar la corrupcion en todas sus manifestaciones. • Fomento de la cultura como la prevencion, procurando nombrar funcionarios honestos y probos conscientes de su mision de servicio a la comunidad. • Fortalecer en area de control interno de la region"},
{"u" : "120000", "o" : "4" , "t" : "m", "n" : 3 , "c" : "1. Fortalecer las capacidades tecnicas de los municipios distritales y provinciales. 2. Implementacion del Sistema Gerencial de Monitoreo de Inversiones."},


{"u" : "120000", "o" : "1920" , "t" : "s", "n" : 0 , "c" : "Promocion de oportunidades y capacidades economicas para las familias en situacion de pobreza."},
{"u" : "120000", "o" : "1920" , "t" : "m", "n" : 0 , "c" : "Reducir los actuales indices de extrema pobreza y pobreza en un 25%, en especial los distritos de la provincia de Pataz y Bolivar."},

{"u" : "120000", "o" : "1920" , "t" : "s", "n" : 1 , "c" : "Lograr una adecuada infraestructura productiva y de servicios, adaptada a la realidad ambiental, en condiciones favorables para el uso sostenible de todos sus recursos, optimizando el alto potencial de estos con la finalidad de contar con una base productiva competitiva y diversificada."},
{"u" : "120000", "o" : "1920" , "t" : "m", "n" : 1 , "c" : "En Alianzas Estrategicas construir 05 Represas en lugares alto andinos que permitan capturar y optimizar el recurso hidrico, ampliando y potencializando la frontera agricola."},

{"u" : "120000", "o" : "1920" , "t" : "s", "n" : 2 , "c" : "Implementacion de los Bonos Habitacionales Familiares Rurales, con la finalidad de generar Valor Agregado ay apego del campesino a su ambito geografico."},
{"u" : "120000", "o" : "1920" , "t" : "m", "n" : 2 , "c" : "Implementar en los 03 distritos mas pobres de la region unos 5,000 Bonos Habitacionales Familiares Rurales."},

{"u" : "120000", "o" : "1920" , "t" : "s", "n" : 3 , "c" : "Interaccion y Articulacion de los Programas Sociales con la REALIDAD socioeconomica de la poblacion de acuerdo a sus potencialidades de desarrollo humano."},
{"u" : "120000", "o" : "1920" , "t" : "m", "n" : 3 , "c" : "No generar un invalido productivo, consumidor de los escasos recursos, sino una persona con DIGNIDAD, consiente que su desarrollo personal y familiar depende de ellos mismos."},


{"u" : "120000", "o" : "55" , "t" : "s", "n" : 0 , "c" : "Deficiente servicio educativo *Mejoramiento del servicio educativo centrado en un presupuesto real. *Disenar un Diseno Curricular relacionado con su realidad geografica. *Programar capacitaciones continuas"},
{"u" : "120000", "o" : "55" , "t" : "s", "n" : 0 , "c" : "Deficiente servicio de salud y falta de centros de salud competentes en eficiencia: Inversion en la infraestructura de nuevos centros de salud y su respectivo equipamiento, tanto material como humano."},
{"u" : "120000", "o" : "55" , "t" : "m", "n" : 0 , "c" : "*Construccion de infraestructura educativas bien equipadas con personal competente e innovador *Curricula exigente centrado en la realidad geografica.. *Realizar dos capacitaciones docentes en el ano en busca de la Calidad Educativa. *Acreditar a los colegios emblematicos en base a la Calidad Educat"},
{"u" : "120000", "o" : "55" , "t" : "m", "n" : 0 , "c" : "*Disminucion de tasa de mortalidad materno infantil en un 25%. *Construccion de 5 centros de salud y su equipamiento respectivo. *Tendido de sistema de redes y conexiones domiciliarias de agua potable y desagüe en las nuevas poblaciones demograficas sin servicios basicos. *Mejoramiento del presupues"},

{"u" : "120000", "o" : "55" , "t" : "s", "n" : 1 , "c" : "Falta de carreteras asfaltadas y conservadas que permitan el acceso de la poblacion andina que conlleven al traslado de su produccion hacia los mercados de consumo. Diagnostico y planificacion de nuevas vias que permitan el desarrollo economico de la poblacion a traves de sus productos de consumo in"},
{"u" : "120000", "o" : "55" , "t" : "s", "n" : 1 , "c" : "Precaria asistencia de servicios en electricidad y canales de irrigacion al servicio del sector productivo. Realizacion de proyectos de electrificacion para el desarrollo agropecuario."},
{"u" : "120000", "o" : "55" , "t" : "s", "n" : 1 , "c" : "El progreso de La Libertad se sustenta en el desarrollo de proyectos motrices La construccion de la III Etapa del proyecto Chavimochic. La construccion de la carretera de Salaverry a Juanjui"},
{"u" : "120000", "o" : "55" , "t" : "m", "n" : 1 , "c" : "- Afirmado de carreteras en base a un estudio tecnico. - Asfaltado de carreteras teniendo como base el estudio tecnico de ingenieria civil de la region. - Construccion de nuevos carreteras segun necesidad de desarrollo. - Mantenimiento de las carreteras."},
{"u" : "120000", "o" : "55" , "t" : "m", "n" : 1 , "c" : "- Electrificacion de acuerdo a estudio de 20 localidades. - Realizacion de conexiones electricas domiciliarias en numero de 9,000 consumidores. - Construir tres canales de riego para el desarrollo de la actividad agropecuaria."},
{"u" : "120000", "o" : "55" , "t" : "m", "n" : 1 , "c" : "- Ejecucion de la presa Palo Redondo de Chavimochic a traves de la inversion privada. - Culminacion de la carretea Salaverry - Juanjui"},

{"u" : "120000", "o" : "55" , "t" : "s", "n" : 2 , "c" : "La falta de una educacion ecologica a llevado al hombre a tomar una actitud depredadora frente a los recursos bioticos y a la diversidad del pais. Elaboracion de planes de contingencia eficaces que permitan conservar el ambiente y bajar los indicadores de afectacion por el calentamiento global."},
{"u" : "120000", "o" : "55" , "t" : "s", "n" : 2 , "c" : "-La falta de tecnicas para el manejo de las cuencas hidricas y reservas acuiferas han debilitado las inversiones para el abastecimiento de aguas de algunas ciudades.Educar a la poblacion en el consumo de agua a fin de ser bien distribuida.Inculpar a la poblacion escolar la importancia del cuidado de"},
{"u" : "120000", "o" : "55" , "t" : "m", "n" : 2 , "c" : "-Disenar, aprobar e implementar un pla eficaz de zonificacion Economica e Ecologica. -Seleccionar de acuerdo a peligrosidad ambiental las areas naturales a proteger en un numero de 4 a razon de una por ano."},
{"u" : "120000", "o" : "55" , "t" : "m", "n" : 2 , "c" : "-Ejecucion de 02 proyectos generados por la cuenca hidrografica del Maranon"},

{"u" : "120000", "o" : "55" , "t" : "s", "n" : 3 , "c" : "-El desconocimiento de las normas de la administracion regional por sus trabajadores hacen que esta se convierta en ineficaz, generando con ello un atraso que afecta al administrado en su solicitud"},
{"u" : "120000", "o" : "55" , "t" : "s", "n" : 3 , "c" : "La inseguridad ciudadana en la region La Libertad, especialmente en las ciudades de Trujillo, Chepen, Pacasmayo, Paijan, Viru se han convertido en entes vulnerables por el aumento de la delincuencia y la falta de estrategias y mecanismo de solucion con los que el gobierno regional no cuenta por su f"},
{"u" : "120000", "o" : "55" , "t" : "m", "n" : 3 , "c" : "Implementacion de cursos de capacitacion versados en la Ley 276 y 27744 y su respectiva reglamentacion.Conocimiento de la Ley del Empleado Publico y su aplicacion en la Etica Profesional. -	02 cursos de capacitacion por ano durante la gestion presidencial. -	Implementacion de un sistema operativo mo"},
{"u" : "120000", "o" : "55" , "t" : "m", "n" : 3 , "c" : "-	Realizar en coordinacion con el sector educacion 06 programas con su respectivo seguimiento en temas como erradicar la delincuencia en su primera fase. - Generar dos proyectos con la participacion del colegio de Psicologos y las universidades locales, la PNP, el Poder Judicial y el Ministerio Publ"},


{"u" : "120000", "o" : "2258" , "t" : "s", "n" : 0 , "c" : "Brindar atencion integral de ninos y ninas menores de cinco anos sobre todo en zonas rurales a traves de las escuelas. Fomentar una educacion tecnica productiva desde los niveles basicos de educacion."},
{"u" : "120000", "o" : "2258" , "t" : "s", "n" : 0 , "c" : "Identificar las zonas de mayor riesgo sanitario, a fin de focalizar el esfuerzo en atencion de salud y nutricion. Atencion integral de ninos y adolecentes tanto en salud y nutricion. Priorizar los sectores mas vulnerables de la sociedad tales como personas con habilidades diferentes, ninos, ancianos"},
{"u" : "120000", "o" : "2258" , "t" : "s", "n" : 0 , "c" : "Creacion de una Red de Proteccion Social Regional destinada a proteger a los segmentos de poblacion mas vulnerables."},
{"u" : "120000", "o" : "2258" , "t" : "m", "n" : 0 , "c" : "Lograr una region comprometida con una educacion de metodologias pedagogicas exitosas que garanticen aprendizajes de calidad. Reducir desercion escolar y la brecha de analfabetismo urbano y rural"},
{"u" : "120000", "o" : "2258" , "t" : "m", "n" : 0 , "c" : "Poblacion regional saludable y alimentada correctamente, con servicios de salud eficientes al alcance de todos."},
{"u" : "120000", "o" : "2258" , "t" : "m", "n" : 0 , "c" : "Desarrollo social a los Libertenos menos favorecidos a traves de propuestas viables y sostenibles."},

{"u" : "120000", "o" : "2258" , "t" : "s", "n" : 1 , "c" : "Promocion de las inversiones publicas y privadas enfocadas a los grandes proyectos de desarrollo que la region necesita."},
{"u" : "120000", "o" : "2258" , "t" : "s", "n" : 1 , "c" : "Potenciar a las pequenas unidades agropecuarias en cada provincia. Impulsar la formacion de micro empresas Agroindustriales sostenibles, mediante capacitacion y facilitarles los tramites con las entidades financieras del sector."},
{"u" : "120000", "o" : "2258" , "t" : "s", "n" : 1 , "c" : "Ordenacion territorial: elaboracion del Plan Director del uso turistico del suelo, del paisaje, de los recursos turisticos y los espacios naturales. Creacion del Observatorio Turistico Regional, como instrumento de gestion de la politica turistica regional, para disponer de informacion precisa."},
{"u" : "120000", "o" : "2258" , "t" : "m", "n" : 1 , "c" : "Al 2018 la region La Libertad se posiciona como la segunda region mas competitiva del Peru."},
{"u" : "120000", "o" : "2258" , "t" : "m", "n" : 1 , "c" : "La Libertad con un sistema macro y micro agropecuario que este en el nivel de las nuevas formas tecnologicas que permitan una produccion superior para el mercado regional, nacional e internacional"},
{"u" : "120000", "o" : "2258" , "t" : "m", "n" : 1 , "c" : "La Libertad se constituye en los primeros destinos turisticos del pais."},

{"u" : "120000", "o" : "2258" , "t" : "s", "n" : 2 , "c" : "Articular las vias regionales mediante la construccion, mejoramiento, rehabilitacion y mantenimiento de infraestructura vial. Incentivar y comprometer la participacion del sector privado en el desarrollo de la infraestructura de transporte en el ambito regional."},
{"u" : "120000", "o" : "2258" , "t" : "s", "n" : 2 , "c" : "Implantar una agresiva politica de electrificacion para llegar a las zonas de dificil acceso. Ejecutar una agresiva politica de dotacion de Proyectos de agua potable, alcantarillado y/o letrinas a todos los pueblos de la Region"},
{"u" : "120000", "o" : "2258" , "t" : "s", "n" : 2 , "c" : "Promover la construccion, mejoramiento y equipamiento de colegios, hospitales, postas medicas, para mejorar los servicios educativos y de salud que la poblacion libertena demanda."},
{"u" : "120000", "o" : "2258" , "t" : "m", "n" : 2 , "c" : "Obtencion de una region sostenible, desarrollada, planificada capaz de mirar a su futuro con la seguridad de crecer en forma ordenada."},
{"u" : "120000", "o" : "2258" , "t" : "m", "n" : 2 , "c" : "La region cuenta con un servicio integral de saneamiento."},
{"u" : "120000", "o" : "2258" , "t" : "m", "n" : 2 , "c" : "La Region cuenta con infraestructuras modernas y equipadas para atencion de la poblacion."},

{"u" : "120000", "o" : "2258" , "t" : "s", "n" : 3 , "c" : "Fortalecer y articular el sistema regional de seguridad ciudadana fomentando la participacion activa a nivel regional, provincial y distrital de las instituciones publicas, privadas y sociedad civil fortaleciendo el sistema de seguridad ciudadana."},
{"u" : "120000", "o" : "2258" , "t" : "s", "n" : 3 , "c" : "Gobierno Regional al servicio del ciudadano para afrontarlos grandes retos, desarrollando una institucionalidad publica eficiente, transparente y promotora y con rendicion de cuentas."},
{"u" : "120000", "o" : "2258" , "t" : "s", "n" : 3 , "c" : "Fomentar la participacion activa a nivel regional, provincial y distrital de las instituciones publicas, privadas y sociedad civil fortaleciendo el sistema de participacion ciudadana."},
{"u" : "120000", "o" : "2258" , "t" : "m", "n" : 3 , "c" : "Sistema regional de seguridad ciudadana, articulado y fortalecido, contando con espacios publicos y carreteras seguras y confiables, contando con un trabajo integrado de Region, Municipalidades Provinciales y PNP, mejorando la economia regional, la confianza interpersonal."},
{"u" : "120000", "o" : "2258" , "t" : "m", "n" : 3 , "c" : "Institucionalizacion en la administracion regional de practicas de buen gobierno, etica, transparencia y lucha contra la corrupcion contribuyendo al desarrollo, el progreso, mejorando la integracion social, la confianza en las instituciones y los derechos de las personas."},
{"u" : "120000", "o" : "2258" , "t" : "m", "n" : 3 , "c" : "Instituciones publicas, privadas, organismos no gubernamentales y sociedad civil participan e intervienen en forma integral en la solucion de los principales problemas de la region."},


{"u" : "120000", "o" : "2628" , "t" : "s", "n" : 0 , "c" : "• Institucionalizar el uso de planes de ordenamiento territorial como parte de la gestion de gobierno local y regional. • Promover la generacion de valor agregado sobre la base de los recursos mineros y de hidrocarburos"},
{"u" : "120000", "o" : "2628" , "t" : "m", "n" : 0 , "c" : "• La productividad de las principales menestras (nuna, arveja, haba, lenteja y tarwi), cereales (quinua, maiz amilaceo y amarillo duro), tuberculos (papa, arracacha, olluco y oca) y frutas (granadilla, yacon, lima y palta) aumenta al menos en un 30% • Incrementar en 30% la superficie agricola bajo"},

{"u" : "120000", "o" : "2628" , "t" : "s", "n" : 1 , "c" : "• Promover la identificacion cultural y conciencia turistica local regional • Promover una gestion participativa y concertada de las estrategias relacionadas al desarrollo del turismo"},
{"u" : "120000", "o" : "2628" , "t" : "m", "n" : 1 , "c" : "• Aumento de arribos turisticos (extranjeros) a tasas anuales de 10%. • Aumentar los dias de permanencia promedio a 3 dias. • Incrementar los productos turisticos tangibles e intangibles en 20% • La ruta Moche posicionada a nivel regional, nacional e internacional"},

{"u" : "120000", "o" : "2628" , "t" : "s", "n" : 2 , "c" : "• Establecer una instancia de coordinacion y concertacion entre Gobierno central, regional y locales (provinciales) orientada a resolver de manera complementaria los problemas prioritarios relacionados a la infraestructura de soporte. • Incentivar el desarrollo de alianzas estrategicas con el secto"},
{"u" : "120000", "o" : "2628" , "t" : "m", "n" : 2 , "c" : "• 12 provincias de la Libertad se encuentran interconectadas vialmente por medio de carreteras asfaltadas y en buen estado • El 50% de la superficie de la red vial se encuentra en buen estado."},

{"u" : "120000", "o" : "2628" , "t" : "s", "n" : 3 , "c" : "• Establecer mecanismos de difusion y promocion para asegurar la participacion activa de las organizaciones sociales de base en los Presupuestos Participativos Anuales."},
{"u" : "120000", "o" : "2628" , "t" : "m", "n" : 3 , "c" : "• Los 4 anos de gestion municipal han promovido la participacion del 85% de las organizaciones sociales de base inscritas en el Gobierno Regional de La Libertad."},


{"u" : "120000", "o" : "15" , "t" : "s", "n" : 0 , "c" : "•Plan Integral de Seguridad."},
{"u" : "120000", "o" : "15" , "t" : "m", "n" : 0 , "c" : "Disminucion dela criminalidad, en el periodo de gestion"},

{"u" : "120000", "o" : "15" , "t" : "s", "n" : 1 , "c" : "GENERAR PUESTO DE TRABAJO EN LAS OBRAS QUE EL GOBIERNO REGIONAL EJECUTE"},
{"u" : "120000", "o" : "15" , "t" : "s", "n" : 1 , "c" : "Desarrollar una industria minera y de hidrocarburos formal y sostenible con productos de alto valor agregado."},
{"u" : "120000", "o" : "15" , "t" : "s", "n" : 1 , "c" : "Posicionar a escala nacional e internacional corredores y circuitos turisticos regionales y macro regionales"},
{"u" : "120000", "o" : "15" , "t" : "m", "n" : 1 , "c" : "10, 000 EMPLEOS ANUALES EN PUESTOS DE TRABAJO GENERADOS EN LA CONSTRUCCION DE OBRAS PUBLICAS QUE EL GOBIERNO REGIONAL EJECUTE"},
{"u" : "120000", "o" : "15" , "t" : "m", "n" : 1 , "c" : "El 80% de la produccion minera y de hidrocarburos se destina a productos con valor agregado. que un 80 % de mineros artesanales se formalicen por el bien de la region."},
{"u" : "120000", "o" : "15" , "t" : "m", "n" : 1 , "c" : "Incrementar los productos turisticos tangibles e intangibles en 80%. La ruta Moche posicionada a nivel regional, nacional e internacional"},

{"u" : "120000", "o" : "15" , "t" : "s", "n" : 3 , "c" : "CHARLAS COMO MEDIO DE PREVENCION PARA LA CONSERVACION DEL MEDIO AMBIENTE"},
{"u" : "120000", "o" : "15" , "t" : "s", "n" : 3 , "c" : "Promover la conservacion del medio ambiente y el manejo sostenible e integrado de los recursos naturales y la biodiversidad"},
{"u" : "120000", "o" : "15" , "t" : "s", "n" : 3 , "c" : "•Establecer una instancia de coordinacion y concentracion entre Gobierno central, regional y locales (provinciales) orientada a resolver de manera complementaria los problemas prioritarios relacionados a la infraestructura de soporte"},
{"u" : "120000", "o" : "15" , "t" : "m", "n" : 3 , "c" : "EN TODA LA REGION SE REALIZARA LAS CAPACITACIONES"},
{"u" : "120000", "o" : "15" , "t" : "m", "n" : 3 , "c" : "El 40% de proyectos relacionados con el medio ambiente se articulan al mercado de bonos de carbono y/o mecanismos similares. reducir a un 90% la contaminacion del agua por parte de las empresas mineras."},
{"u" : "120000", "o" : "15" , "t" : "m", "n" : 3 , "c" : "aumento del presupuesto participativo para nuestra region. que las empresas informales se hayan formalizado para el bien de la region y asi a contribuir para las mejoras como vias de comunicacion, creacion de centros de salud, etc"},

{"u" : "120000", "o" : "15" , "t" : "s", "n" : 3 , "c" : "PLANEAMIENTO ESTRATEGICO PARA LA INTEGRACION ENTRE LAS ORGANIZACIONES SOCIALES DE BASE"},
{"u" : "120000", "o" : "15" , "t" : "s", "n" : 3 , "c" : "Desarrollar una institucionalidad publica eficiente, transparente, promotora y orientada al usuario."},
{"u" : "120000", "o" : "15" , "t" : "s", "n" : 3 , "c" : "Promover la participacion ciudadana democratica y la concertacion en la gestion del desarrollo"},
{"u" : "120000", "o" : "15" , "t" : "m", "n" : 3 , "c" : "LOGRAR LA INTEGRACION EN LAS ORGANIZACIONES DE BASE EN UN 90% DE LAS ORGANIZACIONES SOCIALES DE BASE DEL AMBITO REGIONAL"},
{"u" : "120000", "o" : "15" , "t" : "m", "n" : 3 , "c" : "El 100% de los acuerdos y proyectos plasmados en los Presupuestos Participativos de GR y GL (provinciales), se respetan y ejecutan en los plazos establecidos"},
{"u" : "120000", "o" : "15" , "t" : "m", "n" : 3 , "c" : "consolidar una eficiente labor, gracias a la tecnologia y uso de equipos de ultima generacion para el buen desempeno de nuestras labores"},

]
