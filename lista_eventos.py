eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

ordem_correta = ['Abertura', 'Palestra 2', 'Palestra 3', 'Encerramento']

eventos_registrados.sort(key=ordem_correta.index)

print(eventos_registrados)
