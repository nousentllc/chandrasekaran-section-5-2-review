def run_checks():
    import json
    import numpy as np
    import sympy as sp
    from pathlib import Path
    rng = np.random.default_rng(261134924)
    worst_boost_ratio = 0.0
    min_trace_slack = float('inf')
    min_spread_slack = float('inf')
    for _ in range(500):
        n = int(rng.integers(3, 15))
        k = int(rng.integers(1, n + 1))
        s = rng.uniform(0, 3, n)
        sb, width = 1.5, 2.0
        w = np.exp(-s - (s-sb)**2/(2*width**2))
        c = np.exp(-3) * np.exp(-max(sb**2, (3-sb)**2)/(2*width**2))
        q, _ = np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
        p = q[:,:k] @ q[:,:k].conj().T
        t = np.diag(w)
        tr = np.trace(p @ t).real
        rho = p @ t @ p / tr
        min_trace_slack = min(min_trace_slack, tr-c*k, k-tr)
        s0, delta = 1.5, 0.2
        outside = np.diag((np.abs(s-s0)>delta).astype(float))
        bound = delta**2 + 9*np.trace(p @ outside).real/(c*k)
        moment = np.trace(rho @ np.diag((s-s0)**2)).real
        min_spread_slack = min(min_spread_slack, bound-moment)
        # Vec(CP) has conjugate-side density (PTP)^T; no commuting P assumption.
        psi = (np.diag(np.sqrt(w)) @ p).reshape(-1)/np.sqrt(tr)
        eta = float(rng.uniform(-2,2))
        phases = np.exp(1j*eta*(s-s0)/(2*np.pi))
        boosted = (psi.reshape(n,n)*phases).reshape(-1)
        distance_sq = np.linalg.norm(boosted-psi)**2
        distance_bound = eta**2/(4*np.pi**2)*moment
        assert distance_sq <= distance_bound + 1e-11
        a = rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        a = (a+a.conj().T)/2
        a /= np.linalg.norm(a,2)
        b = rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        b = (b+b.conj().T)/2
        b /= np.linalg.norm(b,2)
        obs = np.kron(a,b)
        change = abs(np.vdot(boosted,obs@boosted)-np.vdot(psi,obs@psi))
        boost_bound = abs(eta)/np.pi*np.sqrt(moment)
        assert change <= boost_bound + 1e-11
        worst_boost_ratio = max(worst_boost_ratio,float(change/boost_bound))
    assert min_trace_slack >= -1e-11
    assert min_spread_slack >= -1e-11
    x = sp.symbols('x', positive=True)
    assert sp.simplify(1-4*x/(1+x)**2-(x-1)**2/(x+1)**2) == 0
    result = {
      'seed':261134924, 'random_trials':500, 'dimension_range':[3,14],
      'trace_lower_and_upper_min_slack':min_trace_slack,
      'spread_bound_min_slack':min_spread_slack,
      'largest_observed_boost_change_over_bound':worst_boost_ratio,
      'symbolic_boost_identity':'verified by exact simplification',
      'countermodel_sections':[{'rank':n,'trace_T_for_T_identity':n,'normalized_rank_one_expectation':1/n} for n in [1,10,100,1000]],
      'scope':'Finite-matrix diagnostics, not a proof of infinite-dimensional or gravitational statements.'
    }
    Path('outputs').mkdir(exist_ok=True)
    Path('outputs/operator_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    run_checks()
