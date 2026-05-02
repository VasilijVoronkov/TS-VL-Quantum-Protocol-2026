Import numpy as np
import matplotlib.pyplot as plt

def simulate_ts_vl():
    # Simulation Parameters
    t = np.linspace(0, 10, 1000)
    
    # 1. Lyapunov Vortex Simulation (Entropy Drainage)
    # Negative exponent ensures stability of the core
    lambda_lyap = -0.6 
    noise_envelope = np.exp(lambda_lyap * t)
    core_signal = noise_envelope * np.sin(2 * np.pi * 2 * t)
    
    # 2. Triangular Synchronization (Phase Locking Dynamics)
    # Node C is the reference; Nodes A and B converge to it
    ref_freq = 0.5
    phase_c = np.mod(2 * np.pi * ref_freq * t, 2 * np.pi)
    # Exponential decay of phase difference
    phase_a = np.mod(phase_c + 1.5 * np.exp(-0.7 * t), 2 * np.pi)
    phase_b = np.mod(phase_c - 1.5 * np.exp(-0.7 * t), 2 * np.pi)

    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Left Plot: Lyapunov Stabilization
    ax1.plot(t, core_signal, color='#00e5ff', label='Stabilized Qubit Core', linewidth=1.5)
    ax1.fill_between(t, -noise_envelope, noise_envelope, color='#0044ff', alpha=0.15, label='Vortex Boundary')
    ax1.set_title("VORONKOV LOOP: LYAPUNOV STABILIZATION", fontweight='bold')
    ax1.set_xlabel("Time (t)")
    ax1.set_ylabel("Amplitude / Phase Coherence")
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Right Plot: Triangular Synchronization
    ax2.plot(t, phase_a, 'r--', label='Node A (Source)', alpha=0.7)
    ax2.plot(t, phase_b, 'g--', label='Node B (Target)', alpha=0.7)
    ax2.plot(t, phase_c, 'k', label='Reference Resonator C', linewidth=2.5)
    ax2.set_title("TRIANGULAR SYNC: PHASE LOCKING", fontweight='bold')
    ax2.set_xlabel("Time (t)")
    ax2.set_ylabel("Phase (rad)")
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulate_ts_vl()
