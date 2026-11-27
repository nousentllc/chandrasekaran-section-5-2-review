def verify_countermodel():
    import json
    import math
    from pathlib import Path
    theta = 0.5
    delta = 1-math.cos(theta)
    q = math.exp(-1/8)
    rows = []
    for extra_cycles in [0,1,10,100]:
        denominator = 3+math.exp(-1)+4*extra_cycles
        response = 2*math.exp(-0.5)/denominator*delta
        norm_squared = q*denominator
        cut_amplitude = norm_squared*(response-delta/2)
        assert response < delta/2
        assert cut_amplitude < 0
        rows.append({'additional_zero_area_cycles':extra_cycles,'normalized_cut_response':response,'cut_X_amplitude':cut_amplitude})
    result = {'theta':theta,'delta':delta,'uncut_X_expectation':delta/2,'cut_results':rows,'scope':'An operator-theoretic separation model; its independently chosen uncut vector does not satisfy the cut-to-uncut gluing identification, and it is not a model of gravitational dynamics.'}
    Path('outputs').mkdir(exist_ok=True)
    Path('outputs/countermodel_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    verify_countermodel()
