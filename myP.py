# Define los patrones y respuestas
patrones = [
    (r'hacer|practicar|disfrutar', [
     '¡Esa actividad suena genial!, que otra cosa deseas realizar']),
    (r'ir|visitar', [
     'se que la pasaras super y no te arrepentiras, con quien o quienes vendras']),
    (r'jugar|participar|asistir',  [
     'se que disfrutaras ese momento, con quien o quienes vendras']),
    (r'ejercicio|actividad',  [
     'con nostros encontraras la mejor activida, con quien o quienes vendras']),
    (r'realizar|explorar|camping',  [
     'Tenemos varias opciones, digita la palabra dia seguido de la fecha que vendras']),
    (r'pasear|paseo|bicicleta|bosque',  [
     'sera lo mejor que viviras,  con quien o quienes vendras']),
    (r'aprender|natación',  ['Esta es tu oportunidad no esperes mas']),
    (r'preparar|ejercicio|actividad',  [
     '¡Esa actividad suena genial!, con quien o quienes vendras']),
    (r'acampar|dormir|aire|estrellas',  [
     'Tendras el mejor descanso, nombra la palabra niños si vendras con niños para ofrecerte mejores opciones']),
    (r'disfrutar|bailar',  [
     'disfrutaremos juntos, digita la palabra dia seguido de la fecha que vendras']),
    (r'relajarse|descansar',  [
     'Tendras el mejor descanso, con quien o quienes vendras ']),
    (r'divertirse|pasarlo|pasarla',  [
     'La pasaras genial, digita la palabra dia seguido de la fecha que vendras']),
    (r'clases|colegio|universidad|libros',  [
     'Esta es tu mejor opcion, digita la palabra dia seguido de la fecha que vendras']),
    (r'baile|cocina|actividad',  [
     '¡Esa actividad suena genial!, con quien o quienes vendras']),
    (r'canoa|velero|varco',  [
     'No te olvidaras de esta experiencia, con quien o quienes vendras']),
    (r'aventuras|excursiones|viajes',  [
     'Lo mejor que viviras, digita la palabra dia seguido de la fecha que vendras']),
    (r'amigos|familia|compañeros',  [
     'Lo mejor es disfrutar estos momentos al lado de las personas queridas, que otra actividad deseas realizar']),
    (r'naturaleza|paisajes|explorar',  [
     '¡Esa actividad suena genial!, con quien o quienes vendras']),
    (r'nadar|busear|',  ['¡Esa actividad suena genial!, con quien o quienes vendras']),
    (r'pescar',  ['no te olvidaras de esta experiencia, con quien o quienes vendras']),
    (r'concierto|festival',  [
     'Podras disfrutar, digita la palabra dia seguido de la fecha que vendras']),
    (r'dia (.*)',  ['Trataremos de brindarte lo mejor ese dia, indica otra activida que deses realizar o digita adios o bye si no nesesitas mas nada']),
    (r'niños',  [
     'para los niños abra un profesor para explicarle mejor, digita la palabra mascostas si vienes con una ']),
    (r'mascotas',  ['tenemos un seguro para tu mascota, si deseas mas informacion digita seguro y te daremos el numero de contacto para que lo puedas adquirir']),
    (r'seguro',  ['este es el numero 300 254 5264']),
    (r'solo|nadien',  [
     ' digita la palabra dia seguido de la fecha que vendras']),
    (r'hola|mucho|gusto',  ['Hola para nosotros es un placer tenerte ']),
    # (r'deporte|ejercicio|actividad',  ['¡Esa actividad suena genial!']),
    # (r'deporte|ejercicio|actividad',  ['¡Esa actividad suena genial!']),
    # (r'deporte|ejercicio|actividad',  ['¡Esa actividad suena genial!']),
    # (r'(\w+)', ['Yes, go on', 'Tell me more', 'I’m listening...']),
    # (r'(.*)', ['Lo siento pero no puedo respoder la pregunta',
    #            'Por favor, repite la pregunta nuevamente', 'No estoy seguro de tu pregunta.'])
]
