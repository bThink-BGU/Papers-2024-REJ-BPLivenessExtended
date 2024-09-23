import numpy as np
import scipy.stats as stats
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest, proportion_confint



data_frames = pd.read_excel('results/results.xlsx', sheet_name=["task 1", "task 2", "task 3", "task 4", "task 5"])

for task_name, df in data_frames.items():
    print(task_name)


    if task_name == "task 5":
        tsr_a = df[df["group"] == "A"]["general correctness"].to_numpy()
        mean_tsr_a = np.mean(tsr_a)
        print("TSR,", round(mean_tsr_a, 3))

        mfur_a = df[df["group"] == "A"]["used must finish"].to_numpy()
        mean_mfur_a = np.mean(mfur_a)
        print("MFUR,", round(mean_mfur_a, 3))

        ptfr_a = df[(df["group"] == "A")&(df["perceived feasibility"] != "-")]["perceived feasibility"].to_numpy()
        ptfr_b = df[(df["group"] == "B")&(df["perceived feasibility"] != "-")]["perceived feasibility"].to_numpy()

        mean_ptfr_a, mean_ptfr_b = np.mean(ptfr_a), np.mean(ptfr_b)
        std_ptfr_a, std_ptfr_b = np.std(ptfr_a), np.std(ptfr_b)
        ptfr_z_stat, ptfr_p_value = proportions_ztest(np.array([sum(ptfr_a), sum(ptfr_b)]), np.array([len(ptfr_a), len(ptfr_b)]))
        print("PTFR,", round(mean_ptfr_a, 3), round(std_ptfr_a, 3), round(mean_ptfr_b, 3), round(std_ptfr_b, 3), round(ptfr_p_value, 3))

        print("PTFR Conf.,", proportion_confint(sum(ptfr_a), len(ptfr_a), 0.05), proportion_confint(sum(ptfr_b), len(ptfr_b), 0.05))
        continue



    tsr_a = df[df["group"] == "A"]["general correctness"].to_numpy()
    tsr_b = df[df["group"] == "B"]["general correctness"].to_numpy()
    cc_a = df[(df["group"] == "A")&(df["general correctness"] == 1)]["cc"].dropna().to_numpy()
    cc_b = df[(df["group"] == "B")&(df["general correctness"] == 1)]["cc"].dropna().to_numpy()
    sloc_a = df[(df["group"] == "A")&(df["general correctness"] == 1)]["sloc"].dropna().to_numpy()
    sloc_b = df[(df["group"] == "B")&(df["general correctness"] == 1)]["sloc"].dropna().to_numpy()
    mfur_a = df[df["group"] == "A"]["used must finish"].to_numpy()

    print("metric, w/ MF, w/o MF, p-value")
    mean_tsr_a, mean_tsr_b = np.mean(tsr_a), np.mean(tsr_b)
    std_tsr_a, std_tsr_b = np.std(tsr_a), np.std(tsr_b)
    tsr_z_stat, tsr_p_value = proportions_ztest(np.array([sum(tsr_a), sum(tsr_b)]), np.array([len(tsr_a), len(tsr_b)]))
    print("TSR,", round(mean_tsr_a, 3), round(std_tsr_a, 3), round(mean_tsr_b, 3), round(std_tsr_b, 3), round(tsr_p_value, 3))

    mean_cc_a, mean_cc_b = np.mean(cc_a), np.mean(cc_b)
    std_cc_a, std_cc_b = np.std(cc_a), np.std(cc_b)
    cc_t_stat, cc_p_value = stats.mannwhitneyu(cc_a, cc_b)
    print("CC,", round(mean_cc_a, 3), round(std_cc_a, 3), round(mean_cc_b, 3), round(std_cc_b, 3), round(cc_p_value, 3))

    mean_sloc_a, mean_sloc_b = np.mean(sloc_a), np.mean(sloc_b)
    std_sloc_a, std_sloc_b = np.std(sloc_a), np.std(sloc_b)
    sloc_t_stat, sloc_p_value = stats.mannwhitneyu(sloc_a, sloc_b)
    print("SLOC,", round(mean_sloc_a, 3), round(std_sloc_a, 3), round(mean_sloc_b, 3), round(std_sloc_b, 3), round(sloc_p_value, 3))

    mean_mfur_a = np.mean(mfur_a)
    mfur_z_stat, mfur_p_value = proportions_ztest(sum(mfur_a), len(mfur_a), value=0)
    print("MFUR,", round(mean_mfur_a, 3), round(mfur_p_value, 3))

    if task_name == "task 5":
        print("TSR Conf.,", proportion_confint(sum(tsr_a), len(tsr_a), 0.05))
        print("MFUR Conf.,", proportion_confint(sum(mfur_a), len(mfur_a), 0.05))



