from Bio import SeqIO
import matplotlib.pyplot as plt

print("Читаю файл ecoli.fasta...")
record = SeqIO.read("ecoli.fasta", "fasta")
genome = record.seq

atg_count = genome.count("ATG")
print(f"Количество старт-кодонов ATG: {atg_count}")

total_codons = len(genome) // 3
other_codons = total_codons - atg_count
print(f"Общее количество кодонов: {total_codons}")
print(f"Количество остальных кодонов: {other_codons}")

labels = ["Старт-кодоны (ATG)", "Другие кодоны"]
sizes = [atg_count, other_codons]
colors = ["red", "blue"]

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title("Соотношение старт-кодонов и остальных кодонов в геноме E. coli")
plt.show()