import numpy as np
import matplotlib.pyplot as plt


def run_wave_simulation(c, dt, dx):

    # =======================
    # Initial condition
    # =======================
    u = np.zeros(200)
    u[10:12] = 10
    u_prev = u.copy()

    lam = (c * dt / dx) ** 2

    # =======================
    # Plot times
    # =======================
    times_to_plot = np.arange(0, 5100, 5100 // 15)

    # =======================
    # Plot setup
    # =======================
    plt.style.use("seaborn-v0_8-whitegrid")

    fig, axes = plt.subplots(
        len(times_to_plot), 2,
        figsize=(15, 5 * len(times_to_plot))
    )

    k = 0

    # =======================
    # Time evolution
    # =======================
    for t in range(5099):

        u_next = np.zeros_like(u)

        for i in range(1, len(u) - 1):
            u_next[i] = (2 * u[i] - u_prev[i] +
                         lam * (u[i+1] - 2*u[i] + u[i-1]))

        u_prev = u.copy()
        u = u_next.copy()

        # =======================
        # Plot selected times
        # =======================
        if t in times_to_plot:

            x = np.arange(len(u))

            # -----------------------
            # FULL SYSTEM
            # -----------------------
            axes[k, 0].plot(x, u, color="royalblue", linewidth=2)
            axes[k, 0].set_title(f"Full system - t = {t*dt:.1f} s",
                                 fontsize=13, fontweight="bold")
            axes[k, 0].set_xlim(0, len(u)-1)
            axes[k, 0].set_xlabel("Position")
            axes[k, 0].set_ylabel("Amplitude")
            axes[k, 0].grid(True, alpha=0.3)
            axes[k, 0].axhline(0, color='black', linewidth=0.8, alpha=0.5)

            # -----------------------
            # ZOOM
            # -----------------------
            threshold = 0.1
            idx = np.where(np.abs(u) > threshold)[0]

            if len(idx) > 0:
                xmin, xmax = idx[0], idx[-1]

                padding = 5
                xmin = max(0, xmin - padding)
                xmax = min(len(u)-1, xmax + padding)

                axes[k, 1].plot(x, u, color="royalblue", linewidth=2, label="u(t)")
                axes[k, 1].plot(x, u_prev, linestyle="--",
                                 color="orange", linewidth=2,
                                 label="u(t - dt)")
                axes[k, 1].set_xlim(xmin, xmax)
                axes[k, 1].set_title("Zoom region",
                                     fontsize=13, fontweight="bold")
                axes[k, 1].set_xlabel("Position")
                axes[k, 1].set_ylabel("Amplitude")
                axes[k, 1].grid(True, alpha=0.3)
                axes[k, 1].axhline(0, color='black', linewidth=0.8, alpha=0.5)
                axes[k, 1].legend()

            else:
                axes[k, 1].set_title("No signal detected")
                axes[k, 1].grid(True, alpha=0.3)

            k += 1

    # =======================
    # Final layout
    # =======================
    plt.tight_layout()
    plt.show()


# =======================
# MAIN
# =======================
if __name__ == "__main__":

    c = 1
    dt = 0.2
    dx = 1

    run_wave_simulation(c, dt, dx)