# Selection of Datasets A to D
def dataset_selector(dataset):

    if dataset == "A":
        filelist = ["N15_M07_F10_K001_1.mat", "N15_M07_F10_K002_1.mat", "N15_M07_F10_K003_1.mat",
                    "N15_M07_F10_K004_1.mat", "N15_M07_F10_K005_1.mat", "N15_M07_F10_K006_1.mat"]
    elif dataset == "B":
        filelist = ["N15_M07_F10_KA01_1.mat", "N15_M07_F10_KA03_1.mat", "N15_M07_F10_KA05_1.mat",
                    "N15_M07_F10_KA06_1.mat", "N15_M07_F10_KA07_1.mat", "N15_M07_F10_KA08_1.mat",
                    "N15_M07_F10_KA09_1.mat", "N15_M07_F10_KI01_1.mat", "N15_M07_F10_KI03_1.mat",
                    "N15_M07_F10_KI05_1.mat", "N15_M07_F10_KI07_1.mat", "N15_M07_F10_KI08_1.mat"]
    elif dataset == "C":
        filelist = ["N15_M07_F10_KA04_1.mat", "N15_M07_F10_KA15_1.mat", "N15_M07_F10_KA16_1.mat",
                    "N15_M07_F10_KA22_1.mat", "N15_M07_F10_KA30_1.mat", "N15_M07_F10_KB23_1.mat",
                    "N15_M07_F10_KB24_1.mat", "N15_M07_F10_KB27_1.mat", "N15_M07_F10_KI04_1.mat",
                    "N15_M07_F10_KI14_1.mat", "N15_M07_F10_KI16_1.mat", "N15_M07_F10_KI17_1.mat",
                    "N15_M07_F10_KI18_1.mat", "N15_M07_F10_KI21_1.mat" ]
    else:
        filelist = ["N15_M07_F10_K001_1.mat", "N15_M07_F10_K002_1.mat", "N15_M07_F10_K003_1.mat",
                    "N15_M07_F10_K004_1.mat", "N15_M07_F10_K005_1.mat", "N15_M07_F10_K006_1.mat",
                    "N15_M07_F10_KA01_1.mat", "N15_M07_F10_KA03_1.mat", "N15_M07_F10_KA04_1.mat",
                    "N15_M07_F10_KA05_1.mat", "N15_M07_F10_KA06_1.mat", "N15_M07_F10_KA07_1.mat",
                    "N15_M07_F10_KA08_1.mat", "N15_M07_F10_KA09_1.mat", "N15_M07_F10_KA15_1.mat",
                    "N15_M07_F10_KA16_1.mat", "N15_M07_F10_KA22_1.mat", "N15_M07_F10_KA30_1.mat",
                    "N15_M07_F10_KB23_1.mat", "N15_M07_F10_KB24_1.mat", "N15_M07_F10_KB27_1.mat",
                    "N15_M07_F10_KI01_1.mat", "N15_M07_F10_KI03_1.mat", "N15_M07_F10_KI04_1.mat",
                    "N15_M07_F10_KI05_1.mat", "N15_M07_F10_KI07_1.mat", "N15_M07_F10_KI08_1.mat",
                    "N15_M07_F10_KI14_1.mat", "N15_M07_F10_KI16_1.mat", "N15_M07_F10_KI17_1.mat",
                    "N15_M07_F10_KI18_1.mat", "N15_M07_F10_KI21_1.mat" ]
    # Bearing Codes
    filelabel = [x[12:16] for x in filelist]
    return filelist, filelabel