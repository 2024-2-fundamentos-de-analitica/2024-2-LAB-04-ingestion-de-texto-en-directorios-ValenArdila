# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
    
"""
La información requerida para este laboratio esta almacenada en el
archivo "files/input.zip" ubicado en la carpeta raíz.
Descomprima este archivo.

Como resultado se creara la carpeta "input" en la raiz del
repositorio, la cual contiene la siguiente estructura de archivos:


```
train/
    negative/
        0000.txt
        0001.txt
        ...
    positive/
        0000.txt
        0001.txt
        ...
    neutral/
        0000.txt
        0001.txt
        ...
test/
    negative/
        0000.txt
        0001.txt
        ...
    positive/
        0000.txt
        0001.txt
        ...
    neutral/
        0000.txt
        0001.txt
        ...
```

A partir de esta informacion escriba el código que permita generar
dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
del repositorio.

Estos archivos deben tener la siguiente estructura:

* phrase: Texto de la frase. hay una frase por cada archivo de texto.
* sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
    o "neutral". Este corresponde al nombre del directorio donde se
    encuentra ubicado el archivo.

Cada archivo tendria una estructura similar a la siguiente:

```
|    | phrase                                                                                                                                                                 | target   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
|  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
|  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
|  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
|  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
```


"""
import os
import zipfile
import pandas as pd

def pregunta_01():
    # Ruta del archivo zip de entrada y carpetas de salida
    zip_path = "files/input.zip"
    extracted_folder = "files/input"  # Cambiado para coincidir con la estructura esperada
    output_csv_folder = "files/output"  # Aseguramos que sea 'output'

    # Descomprimir el archivo ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extracted_folder)

    # Crear una lista para almacenar los datos de train y test
    datatrain = []
    datatest = []
    
    
    
    # Recorrer los directorios de train y test
    
    for folder in ["test", "train"]:
        for sentiment in ["negative", "positive", "neutral"]:
            for filename in os.listdir(f"{extracted_folder}/{"input"}/{folder}/{sentiment}"):
                with open(f"{extracted_folder}/{"input"}/{folder}/{sentiment}/{filename}") as f:
                    phrase = f.read()
                    if folder == "train":
                        datatrain.append({"phrase": phrase, "target": sentiment})
                    else:
                        datatest.append({"phrase": phrase, "target": sentiment})
                        
    # Crear un DataFrame con los datos de train y test
    df_train = pd.DataFrame(datatrain)
    df_test = pd.DataFrame(datatest)
    
    # Guardar los DataFrames en archivos CSV
    
    if not os.path.exists(output_csv_folder):
        os.makedirs(output_csv_folder)
    df_train.to_csv(f"{output_csv_folder}/train_dataset.csv", index=False)
    df_test.to_csv(f"{output_csv_folder}/test_dataset.csv", index=False)
    
