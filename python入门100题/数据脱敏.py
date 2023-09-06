

import re

content = "hello hello Xiao Sunqiang 17838599899"


pattern = r"1[3-9]\d{9}"


result = re.sub(pattern, "1***", content )
print(result)