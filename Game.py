"""
Q-Orbit: Quantum Space Mission Designer (Playable Game)
NASA Space Apps Challenge 2026 - Space Mission Design Game
Author: mamtagupta1986mgs-spec
License: MIT License
"""

import math
import time

# Official NASA JPL Horizons Constants
MU_SUN_KM3_S2 = 1.32712440018e11  # Solar gravitational parameter (km^3/s^2)
G0_M_S2 = 9.80665                 # Standard gravity (m/s^2)
AU_KM = 149597870.7               # 1 Astronomical Unit (km)

ORBITAL_RADII_KM = {
    "Earth": 1.000 * AU_KM,
    "Mars": 1.524 * AU_KM,
    "Venus": 0.723 * AU_KM,
}

# Candidate Rocket Propulsion Stages (NASA LSP Benchmarks)
PROPULSION_OPTIONS = [
    {
        "id": 1,
        "name": "LOX/LH2 Cryogenic Upper Stage",
        "isp_s": 450.0,
        "dry_mass_kg": 3200.0,
        "cost_m": 85.0,
        "max_propellant_kg": 28000.0,
    },
    {
        "id": 2,
        "name": "LOX/CH4 Methalox Stage",
        "isp_s": 380.0,
        "dry_mass_kg": 4100.0,
        "cost_m": 60.0,
        "max_propellant_kg": 45000.0,
    },
    {
        "id": 3,
        "name": "Nuclear Thermal Propulsion (NTP)",
        "isp_s": 900.0,
        "dry_mass_kg": 5500.0,
        "cost_m": 165.0,
        "max_propellant_kg": 18000.0,
    },
]


def vis_viva_velocity_km_s(mu: float, r_km: float, a_km: float) -> float:
    """Computes orbital velocity (km/s) via the Vis-Viva equation."""
    return math.sqrt(mu * ((2.0 / r_km) - (1.0 / a_km)))


def hohmann_transfer_delta_v_m_s(origin: str, destination: str):
    """Calculates Hohmann transfer departure, arrival, and total Delta-V (m/s)."""
    r1 = ORBITAL_RADII_KM[origin]
    r2 = ORBITAL_RADII_KM[destination]
    a_transfer = 0.5 * (r1 + r2)

    v_origin = math.sqrt(MU_SUN_KM3_S2 / r1)
    v_dest = math.sqrt(MU_SUN_KM3_S2 / r2)

    v_dep = vis_viva_velocity_km_s(MU_SUN_KM3_S2, r1, a_transfer)
    v_arr = vis_viva_velocity_km_s(MU_SUN_KM3_S2, r2, a_transfer)

    dv1_m_s = abs(v_dep - v_origin) * 1000.0
    dv2_m_s = abs(v_dest - v_arr) * 1000.0
    return dv1_m_s, dv2_m_s, (dv1_m_s + dv2_m_s)


def required_propellant_mass_kg(delta_v_m_s: float, isp_s: float, dry_plus_payload_kg: float) -> float:
    """Inverts the Tsiolkovsky rocket equation to compute required propellant (kg)."""
    mass_ratio = math.exp(delta_v_m_s / (isp_s * G0_M_S2))
    initial_mass_kg = dry_plus_payload_kg * mass_ratio
    return initial_mass_kg - dry_plus_payload_kg


def quantum_qubo_stage_selector(total_dv_m_s: float, payload_kg: float, max_budget_m: float):
    """Quantum-inspired QUBO solver minimizing propellant mass + budget violation penalty."""
    best_stage = None
    best_hamiltonian = float("inf")
    results = []

    for stage in PROPULSION_OPTIONS:
        total_dry = stage["dry_mass_kg"] + payload_kg
        prop_mass = required_propellant_mass_kg(total_dv_m_s, stage["isp_s"], total_dry)

        budget_violation = max(0.0, stage["cost_m"] - max_budget_m)
        tank_violation = max(0.0, prop_mass - stage["max_propellant_kg"])
        penalty = 50000.0 * (budget_violation + (tank_violation / 100.0))
        hamiltonian = prop_mass + penalty

        results.append((stage, prop_mass, hamiltonian, budget_violation == 0 and tank_violation == 0))

        if hamiltonian < best_hamiltonian:
            best_hamiltonian = hamiltonian
            best_stage = stage

    return best_stage, results


def play_game():
    print("=" * 64)
    print("🚀 Q-ORBIT: QUANTUM SPACE MISSION DESIGNER (NASA JPL EDITION)")
    print("=" * 64)

    while True:
        print("\nSTEP 1: Choose Destination from Earth (1.000 AU)")
        print("  Mars  (1.524 AU - Red Planet Orbit Insertion)")
        print("  Venus (0.723 AU - Inner Solar System Transfer)")
        dest_choice = input("Select target [1 or 2]: ").strip()
        destination = "Venus" if dest_choice == "2" else "Mars"

        dv1, dv2, total_dv = hohmann_transfer_delta_v_m_s("Earth", destination)
        print(f"\n📡 NASA JPL Hohmann Transfer Telemetry (Earth -> {destination}):")
        print(f"   • Departure Burn (Δv1): {dv1:,.1f} m/s")
        print(f"   • Arrival Burn   (Δv2): {dv2:,.1f} m/s")
        print(f"   • Total Mission  (Δv) : {total_dv:,.1f} m/s")

        print("\nSTEP 2: Configure Spacecraft Payload & Mission Budget")
        try:
            payload_kg = float(input("Enter Scientific Payload Mass in kg (e.g., 1500): ").strip())
            max_budget_m = float(input("Enter Maximum Mission Budget in $M (e.g., 100): ").strip())
        except ValueError:
            print("⚠️ Invalid number entered. Using default: 1,500 kg payload & $100M budget.")
            payload_kg = 1500.0
            max_budget_m = 100.0

        print("\nSTEP 3: Choose Propulsion Stage (or enter for Quantum QUBO Auto-Optimize)")
        for s in PROPULSION_OPTIONS:
            print(f"  [{s['id']}] {s['name']} | Isp: {s['isp_s']}s | Dry: {s['dry_mass_kg']}kg | Cost: ${s['cost_m']}M")
        print("  ⚛️  Run Quantum-Inspired QUBO Stage Optimizer")

        stage_choice = input("Your choice [0-3]: ").strip()
        optimal_stage, all_evals = quantum_qubo_stage_selector(total_dv, payload_kg, max_budget_m)

        if stage_choice == "0":
            selected_stage = optimal_stage
            print(f"\n⚛️  QUBO Solver Selected: {selected_stage['name']}")
        else:
            idx = int(stage_choice) - 1 if stage_choice in ["1", "2", "3"] else 0
            selected_stage = PROPULSION_OPTIONS[idx]

        print("\n🔥 INITIATING HOHMANN TRANSFER SIMULATION...")
        for step in ["[T-00:03] Main Engine Start...", "[T+02:15] Parking Orbit Achieved...", f"[T+180d] Approaching {destination}..."]:
            print(f"   {step}")
            time.sleep(0.5)

        total_dry = selected_stage["dry_mass_kg"] + payload_kg
        prop_needed = required_propellant_mass_kg(total_dv, selected_stage["isp_s"], total_dry)
        wet_mass = total_dry + prop_needed

        print("\n" + "=" * 64)
        print("📊 FINAL MISSION TELEMETRY REPORT")
        print("=" * 64)
        print(f"Target Planet      : {destination}")
        print(f"Propulsion Stage   : {selected_stage['name']}")
        print(f"Required Propellant: {prop_needed:,.1f} kg (Max Tank: {selected_stage['max_propellant_kg']:,.0f} kg)")
        print(f"Total Launch Mass  : {wet_mass:,.1f} kg")
        print(f"Mission Cost       : ${selected_stage['cost_m']:.1f}M (Budget Limit: ${max_budget_m:.1f}M)")

        within_budget = selected_stage["cost_m"] <= max_budget_m
        within_fuel = prop_needed <= selected_stage["max_propellant_kg"]

        if within_budget and within_fuel:
            print("\n✅ MISSION SUCCESS! Spacecraft entered stable orbit around", destination + "!")
            if selected_stage["id"] == optimal_stage["id"]:
                print("🏆 BONUS: You matched the Quantum QUBO Global Optimum!")
        else:
            print("\n❌ MISSION FAILED!")
            if not within_budget:
                print(f"   • Budget Exceeded by ${selected_stage['cost_m'] - max_budget_m:.1f}M.")
            if not within_fuel:
                print(f"   • Propellant Overload: Needed {prop_needed:,.0f} kg, exceeding tank capacity.")
            print(f"   💡 Tip: QUBO Optimal Choice was '{optimal_stage['name']}'.")

        again = input("\nDesign another mission? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing Q-Orbit! Safe travels across the Solar System. 🚀")
            break


if __name__ == "__main__":
    play_game()
                      
