
def rank_clients(input_list_of_dict, ranking_func):
    
    headers=list(input_list_of_dict[0].keys())
    rows=[list(x.values()) for x in input_list_of_dict]

    # print(rows)
    # print(headers)

    scored_rows = [(row, ranking_func(row, headers)) for row in rows]
    #print(headers)
    sorted_rows = sorted(scored_rows, key=lambda x: x[1], reverse=True)

    print(sorted_rows[-1])
    
    just_rows=[(x[0][1:]) for x in sorted_rows] # just rows without score and without id + relevant_score
    
    for i in range(0,len(just_rows)):
        just_rows[i].append(sorted_rows[i][1])
    
    print("----------------------------------------------------")
    headers=headers[1:]
    headers.append("relevant_score")
    #print(headers)
    print(just_rows[-1])
    
    list_of_dicts = [dict(zip(headers, values)) for values in just_rows]
    
    #print(list_of_dicts[-1])
    #print("\n====================================================================\n")
    
    return list_of_dicts
    