from base.base import Base

class AppBase(Base):
    def app_base_is_exit(self,loc):
        try:
            self.base_find(loc, timeout= 5)
            print("找到指定元素{}".format(loc))
            return True
        except:
            print("未找到指定元素{}".format(loc))
            return False