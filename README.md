Convertidor de IPs a Objetos Cisco (GUI)

Este programa en Python proporciona una interfaz gráfica para convertir una lista de direcciones IP en formato de objetos Cisco ASA (por ejemplo, "network-object host 192.168.0.1").

Está diseñado para facilitar la generación masiva de objetos a partir de texto con IPs copiadas de reportes, correos, o archivos diversos.

Requisitos:
- Python 3.x
- Módulos: tkinter, pyperclip

Ejemplo de uso:
1. Copia un texto que contenga varias IPs.
2. Pega las IPs en el primer cuadro de texto.
3. Presiona "Procesar" para convertir cada IP en formato Cisco.
4. Copia el resultado con el botón "Copiar resultado".

Este script detecta automáticamente IPs separadas por saltos de línea, espacios u otros caracteres no numéricos.
