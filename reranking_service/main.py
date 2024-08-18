import asyncio
from clients_reranking.main import main

from apscheduler.schedulers.blocking import BlockingScheduler
from push_db.main import main as fill
if __name__=="__main__":
    fill()
    asyncio.run(main())
    #scheduler = BlockingScheduler()
    #scheduler.add_job(main, 'interval', hours=1)
    
    
    
    
    # scheduler.add_job(main, 'interval', seconds=10)
    # scheduler.start()