import asyncio
from clients_reranking.ml_models.expobank_reranker import calculate_score_expobank
from clients_reranking.ml_models.includes import *
from .collect_data import collect_data
from .ml_models.rank_clients import rank_clients

from .write_data import write_to_table

async def main():
    all_users=await collect_data("hackaton_client_data")
    # print(all_users[-1])
    # print("\n================================================================\n")
    print("I`ve collected data")
    autoexpress_sorted_users=rank_clients(all_users,calculate_score_autoexpress)
    print("I`ve reranked autoexpress")
    d2_sorted_users=rank_clients(all_users,calculate_score_d2)
    print("I`ve reranked d2")
    expocar_sorted_users=rank_clients(all_users,calculate_score_expocar)
    print("I`ve reranked expocar")
    hvoya_sorted_users=rank_clients(all_users,calculate_score_park_hotel)
    print("I`ve reranked hvoya")
    leasing_sorted_users=rank_clients(all_users,calculate_score_leasing)
    print("I`ve reranked leasing")
    expobank_sorted_users=rank_clients(all_users,calculate_score_expobank)
    print("I`ve reranked expobank")
    
    
    
    
    # write_to_table("sorted_autoexpress",autoexpress_sorted_users)
    # write_to_table("sorted_d2",d2_sorted_users)
    # write_to_table("sorted_expocar",expocar_sorted_users)
    # write_to_table("sorted_hvoya",hvoya_sorted_users)
    # write_to_table("sorted_leasing",leasing_sorted_users)
    # write_to_table("sorted_expobank",expobank_sorted_users)
    tasks = [
        asyncio.create_task(write_to_table("sorted_autoexpress", autoexpress_sorted_users)),#
        asyncio.create_task(write_to_table("sorted_d2", d2_sorted_users)),#
        asyncio.create_task(write_to_table("sorted_expocar", expocar_sorted_users)),
        asyncio.create_task(write_to_table("sorted_hvoya", hvoya_sorted_users)),#
        asyncio.create_task(write_to_table("sorted_leasing", leasing_sorted_users)),#
        asyncio.create_task(write_to_table("sorted_expobank",expobank_sorted_users)) #
    ]
    
    # Ожидаем выполнения всех задач
    await asyncio.gather(*tasks)
    
    
    
    

    