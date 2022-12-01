import pandas as pd

# filename = "mega_sena_asloterias_ate_concurso_2544_sorteio.xlsx"
filename = "mega_sena_asloterias_ate_concurso_2544_sorteio - alterada.xlsx"

# por bola/coluna onde [] se coloca o index da coluna desejada
pd.set_option("display.max_rows", 1000)
df = pd.read_excel(filename, header=None, index_col=False)[0]

print(df.value_counts())
