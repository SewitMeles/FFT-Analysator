#Script für das Preprocessing. Beispiel Auswahl der Kanäle oder ähnliches.
import h5py
import io
import numpy as np

class Preprocess:

    def __init__(self, binary_file):

        self.binary_file = binary_file
        self.converted_file = self.convert_data(self.binary_file)

        self.channel_count = None
        self.channel_size = None
        self.selected_channel_data = None
        self.data = None

    def get_channel_data(self, channel):
        data = np.array(self.converted_file[:])[:, channel]

        return data

    def get_channel_size(self, channel):
        size = np.array(self.converted_file[:])[:, channel].shape[0]

        return size

    def get_channel_count(self):
        count = np.array(self.converted_file[:]).shape[1]
        
        return count

    def get_abtastrate(self):
        # Muss noch befüllt werden. Vermutlich bietet Acourlar hier eine Funktion oder es kann aus dem Datenset
        # gelesen werden
        return None
    
    def convert_data(self, file_data):
        # Erstelle ein file-like object aus den Bytes
        #print(io.BytesIO(file_data))
        with h5py.File(io.BytesIO(self.binary_file[0]), 'r') as file:
            # Zugriff auf den gewünschten Datensatz
            data = file['time_data'][:]

        return data