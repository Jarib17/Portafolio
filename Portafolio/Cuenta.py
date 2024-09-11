__author__ = "Andres Jarib Quiñones"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "andres.quinones@campusucc.edu.co"

from Cuenta_ahorros import cuenta_ahorros
from Cuenta_cdt import Cuenta_cdt
from Cuenta_corriente import cuenta_Corriente

class cuenta:

    # Aquí inicia la declaracion de la clase
    
    """#----------------------------------------------------------------
    # Atributos 
    ----------------------------------------------------------------#"""
    
    nombre = ""
    apellido = ""
    numero_de_documento = 0
    
    """#----------------------------------------------------------------
    # 1 = Cuenta_ahorros , 2 = Cuenta_Cdt , 3 = Cuenta_corriente
    ----------------------------------------------------------------#"""
