from qiskit import Aer, QuantumCircuit, transpile, assemble
from qiskit.visualization import plot_histogram


def basic_math_circuit():
    n = 7  # Number of qubits
    
    circuit = QuantumCircuit(n, n)
    circuit.h(range(n))
    circuit.cx(0, 1) 
    
    circuit.measure(range(n), range(n))  
    
    return circuit


simulator = Aer.get_backend('aer_simulator')
t_circuit = transpile(basic_math_circuit(), simulator)
qobj = assemble(t_circuit)
result = simulator.run(qobj).result()

# Display results
counts = result.get_counts()

print("Measurement results:", counts)

plot_histogram(counts)
