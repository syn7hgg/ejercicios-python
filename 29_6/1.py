import matplotlib

import pandas

archivo_csv = "vacunados_covid_17-40.csv"


def graficas():
    datos = pandas.read_csv(archivo_csv)

    with open(archivo_csv) as myfile:
        total_lines = sum(1 for line in myfile)

    # print(total_lines)

    contar = total_lines - 1

    print("Inicio de Gráficas")

    df = datos[
        ["Region", "Dosis", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31",
         "32", "33", "34", "35", "36", "37", "38", "39", "40"]]

    df = datos.rename(columns={"Region": "Region", "Dosis": "Dosis", "17": "Edad_17", "18": "Edad_18", "19": "Edad_19",
                               "20": "Edad_20", "21": "Edad_21", "22": "Edad_22", "23": "Edad_23", "24": "Edad_24",
                               "25": "Edad_25", "26": "Edad_26", "27": "Edad_27", "28": "Edad_28", "29": "Edad_29",
                               "30": "Edad_30", "31": "Edad_31", "32": "Edad_32", "33": "Edad_33", "34": "Edad_34",
                               "35": "Edad_35", "36": "Edad_36", "37": "Edad_37", "38": "Edad_38", "39": "Edad_39",
                               "40": "Edad_40"})

    print("1 Impresión normal por interprete")

    print(df.sample(contar))

    print("2 Impresion Histograma")

    print("2.1 Impresion Histograma para 17 años")

    df.Edad_17.plot.hist()

    matplotlib.pyplot.show()

    print("2.2 Impresion Histograma para 18 años")

    df.Edad_18.plot.hist()

    matplotlib.pyplot.show()

    print("2.3 Impresion Histograma para 19 años")

    df.Edad_19.plot.hist()

    matplotlib.pyplot.show()

    print("2.4 Impresion Histograma para 20 años")

    df.Edad_20.plot.hist()

    matplotlib.pyplot.show()

    print("2.5 Impresion Histograma para 21 años")

    df.Edad_21.plot.hist()

    matplotlib.pyplot.show()

    print("2.6 Impresion Histograma para 22 años")

    df.Edad_22.plot.hist()

    matplotlib.pyplot.show()

    print("2.7 Impresion Histograma para 23 años")

    df.Edad_23.plot.hist()

    matplotlib.pyplot.show()

    print("2.8 Impresion Histograma para 25 años")

    df.Edad_25.plot.hist()

    matplotlib.pyplot.show()

    print("2.9 Impresion Histograma para 30 años")

    df.Edad_30.plot.hist()

    matplotlib.pyplot.show()

    print("2.10 Impresion Histograma para 35 años")

    df.Edad_35.plot.hist()

    matplotlib.pyplot.show()

    print("2.11 Impresion Histograma para 40 años")

    df.Edad_40.plot.hist()

    matplotlib.pyplot.show()

    print("2.12 Impresion Histograma de 17 a 40 años")

    df.plot.hist()

    matplotlib.pyplot.show()

    print("3 Impresión histograma frecuencia")

    df.plot.hist(bins=1000, xlim=(0, 3000))

    matplotlib.pyplot.show()

    print("4 Impresión histograma dispersion")

    df.plot.scatter(x="Region", y="Edad_40", alpha=0.5)

    matplotlib.pyplot.show()

    print("5 Impresión histograma X e Y")

    NOMBRE = df.groupby("Region")["Edad_40"].mean()

    NOMBRE.head(20).plot.barh()

    matplotlib.pyplot.show()

    print("6 Impresión dispersion impacto")

    df["Region"] = pandas.qcut(df.Edad_40, 25)

    df.boxplot(column="Edad_40", by="Region", figsize=(8, 6))

    matplotlib.pyplot.show()

    print("7.1 Impresión gráfico de torta por Region")

    df.Region.value_counts().plot.pie()

    matplotlib.pyplot.show()

    print("7.2 Impresión gráfico de torta por rango 40 años")

    df.Edad_40.value_counts().plot.pie()

    matplotlib.pyplot.show()

    print("7.3 Impresión gráfico de torta")

    df.value_counts().plot.pie()

    matplotlib.pyplot.show()

    return print("Fin gráfica")


graficas()
