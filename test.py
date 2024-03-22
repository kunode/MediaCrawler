import argparse
import asyncio
import sys

import config
from base.base_crawler import AbstractCrawler

from media_platform.xhs import XiaoHongShuCrawler


async def main():
    # define command line params ...

    crawler = XiaoHongShuCrawler()
    crawler.init_config(
        platform='xhs',
        login_type='qrcode',
        crawler_type='detail'
    )
    await crawler.start()


if __name__ == '__main__':
    try:
        # asyncio.run(main())
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        sys.exit()
