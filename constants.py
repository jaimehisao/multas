
# Endpoints of ASP backends from where the tickets will be retrieved.
SAN_PEDRO_ASP_ENDPOINT = "https://aplicativos.sanpedro.gob.mx/esanpedro/multas/estado_cuenta.asp"
MONTERREY_ASP_ENDPOINT = "https://asp.monterrey.gob.mx/MultasTransito/"

# Sets the amount of plates that will be considered candidates after a positive match.
CANDIDATE_PLATES_AFTER_POSITIVE_MATCH = 20 + 1

# Sets the minimum time of days when a plate will be queried again, this to provide all plates an equal chance.
QUERY_COOLDOWN_DAYS = 90
