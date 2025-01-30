from qiskit import QuantumCircuit, Aer, execute

# 1 kübit ve 1 klasik bit içeren kuantum devresi oluştur
qc = QuantumCircuit(1, 1)

# Hadamard kapısı (H) ile kübiti süperpozisyona sok
qc.h(0)

# Kübiti ölç ve klasik bite kaydet
qc.measure(0, 0)

# Simülatörde çalıştır
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1000).result()

# Ölçüm sonuçlarını yazdır
counts = result.get_counts()
print("Ölçüm Sonuçları:", counts)

# Devreyi görselleştir
qc.draw('mpl')
