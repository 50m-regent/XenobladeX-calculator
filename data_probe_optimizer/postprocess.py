from .type import ProbeType


def sanitize_probes(probes: dict[int, ProbeType]) -> dict[int, ProbeType]:
    sanitized = {}
    for site in probes.keys():
        if probes[site] == ProbeType.BASIC:
            continue
        sanitized[site] = probes[site]

    return sanitized
