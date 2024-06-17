def sort_matches_by_date(matches):
    response = []

    current_matches = []
    for i in range(len(matches)):
        current_matches.append(matches[i])
        if i < len(matches) - 1:
            if matches[i].date != matches[i + 1].date:
                response.append({"date": matches[i].date, "matches": current_matches})
                current_matches = []

    response.append({"date": matches[i].date, "matches": current_matches})

    return response
