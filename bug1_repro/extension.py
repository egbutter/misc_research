import pandas as pd
from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities

#start_session = pd.Timestamp('1991-01-02', tz='utc')
#end_session = pd.Timestamp('2017-12-29', tz='utc')

start_session = pd.Timestamp('2014-01-28', tz='utc')
end_session = pd.Timestamp('2014-02-07', tz='utc')

register(
    'csvdir',
    csvdir_equities(
        ["daily"],
#        '/Users/jonathan/devwork/misc_research/futures'
         '/Users/jonathan/devwork/misc_research/bug1_repro/data'
    ),
    start_session=start_session,
    end_session=end_session
)
