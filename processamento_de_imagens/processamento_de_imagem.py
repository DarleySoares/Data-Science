from os import listdir
from numpy import asarray
from numpy import save
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

# definicação da pasta onde estão as imagens
folder = 'train/'
photos, labels = list(), list()

# classifica as fotos por categoria / enumeração
for file in listdir(folder):
    # determina 0 para cachorros
    output = 0
    # determina 1 para gatos
    if file.startswith('cat'):
        output = 1
        
    # carrega a imagem
    photo = load_img(folder + file, target_size = (50,50))
    
    # converte foto para vetor numpy
    photo = img_to_array(photo)

    # armazena imagem e label na lista
    photos.append(photo)
    labels.append(output)

# converte as litas para vetores numpy
photos = asarray(photos)
labels = asarray(labels)

print(photos.shape, labels.shape)

# salva fotos no formato de vetor numpy
save('dogs_vs_cats_photos.npy', photos)
save('dogs_vs_cats_labels.npy', labels)

# criação de diretórios para separar as imagens
dataset_path = 'dataset_dogs_vs_cats/'
subdirs = ['train/', 'test/']

for subdir in subdirs:
    # cria os subdiretórios referentes as categorias
    labelsdir  =  ['cats/',  'dogs/']
    
    for labeldir in labelsdir:
        newdir = dataset_path + subdir + labeldir
        makedirs(newdir, exist_ok = True)

