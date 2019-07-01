#!/usr/bin/env python
# coding: utf-8

# In[1]:


import this


# In[2]:


# 파이썬의 철학이다


# In[4]:


import antigravity


# In[5]:


# 지금 안나오는데, 이를 통해 파이썬의 철학을 알 수 있음


# In[6]:


# 함수형 패러다임을 쓸 수 있다 !!


# In[7]:





# # 할당(assignment) : 나중에 사용하기 위해 이름을 붙이는 것

# In[9]:


# 다른 언어랑 다르게, 타입을 정하지 않고 사용한다
# dynamic type
# 자료 타입을 안써도 자동으로 할당을 한다


# In[11]:


# 1. 할당 = 메모리의 공간을 확보한다
# 2. 그 이름이 binding된다


# ###

# In[12]:


a = 1


# In[13]:


a = b = 2


# ## --------------------------------------------------------------------------------------

# In[ ]:





# # 완전 기초부터

# ## [파이썬 장점]
# #### - 자동화 시스템
# #### 인스타그램, ai 등에서 파이썬을 통해 사용
# #### 전 세계에서 가장 많이 사용하는 언어
# ## [단점]
# #### - 속도가 느리다

# ### ^배우기 쉽고 강력하다^
# ### ^효율적인 자료구조^
# ### ^객체지향^

# ## 1. 파이썬의 숫자형(4개)
# ####  int float complex bool 
# 
# ## 2. 문자형(3개)
# #### str bite bitearray
# 
# ### 합쳐서 관리(블로그 찾아보기)
# ### container형 - list는 mutable, tuple는 immutable, 순서도 중복도 없는 set 타입(mutable), prozen set, dictionary type
# ### con

# In[ ]:





# ### ! 파이썬의 객체지향기법 
# ### - 못하는 것이 없다
# ### =>> 함수가 객체여야 한다

# ### ! functional 패러다임
# ### - list 같은 여러가지 묶음을 한꺼번에 처리해준다, 생산성도 높다 -> 빅데이터 처리에 good

# ### 시간, 메모리 사용량, 코드 길이 등등이 성능을 평가하는 요소

# ### ! 파이썬은 glue language
# ### - c로 만든 언어
# ### - pypy -> stackless, 파이썬보다 5배는 빠르다

# In[ ]:





# ## 프로그래밍
# ### : 문법(키워드, 식, 문)을 이용해서 값을 입력받고, 계산/변환하고, 출력하여 흐름을 만드는 일

# In[ ]:





# # ------- - - - - - - - - - - - -------------------------------------------------------------------------

# In[14]:


import keyword


# In[17]:


dir(keyword) #객체지향에서 사용하는 attribute를 확인하는 방법


# In[18]:


# 언더바 2개가 붙은 것 : magic method
# kw : keyword의 줄임말
# kwlist는 키워드 list를 보여주는 것이다


# In[20]:


keyword.kwlist # 현재 버전에서 사용할 수 있는 키워드가 나온다


# In[21]:


# list의 컨테이너 개수를 len으로 확인할 수 있다


# In[22]:


len(keyword.kwlist)


# In[23]:


# 1주차에서는 33개만 배운다(await, async는 고급과정)


# In[ ]:





# # 할당문

# In[24]:


a = 1


# #### = 기준으로 왼쪽에는 변수라고 하면 반만 맞다(lambda는 수가 아니기 때문이다), 그래서 식별자(indentifier)라고 한다
# #### = 기준으로 오른쪽에는 표현식이 나온다

# ### 식은 하나의 결과값으로 축약할 수 있는 것

# In[27]:


a = 1+2 # 이렇게 축약할 수 있는 애를 식이라고 한다


# In[28]:


a


# In[34]:


# coding style guide에서 이름을 어떻게 붙이는지 약속이 되어 있다(pep8 coding style guide)


# ### 카넬 방식 : 두 단어를 이을 때 (30:30)

# In[32]:


# moonBeauty


# ### snake 방식 : 함수 이름 만들 때

# In[33]:


# moon_beauty


# In[35]:


# 관례상 상수는 다 대문자
# 파이썬은 상수가 없다. 일반적인 방식으로 강제시킬 수 없다


# In[36]:


문근영 = 1


# In[37]:


문근영


# In[38]:


# 한글도 언어상 문제 없이 호출되지만, 기본적으로는 unicode 쓰지말고 a-z 사이에만 사용
# 숫자는 사용 안돼
# 특수문자는 예외적으로 언더바 쓰면 되는 애가 있다 


# In[39]:


get_ipython().system('문근영 = 1')


# In[40]:


^문근영 = 1


# In[41]:


_문근영 = 1


# In[42]:


# 언더바 1개 : import * 할 때 import가 안된다


# In[44]:


# 파이썬은 오른쪽에 조건식 또는 함수가 올 수도 있다


# In[43]:


a = 1
b = 3 if a>0 else 5


# In[45]:


# 1. 1이라는 것이 메모리 공간에 할당된다
# 2. namespace에 a가 할당된다


# In[49]:


x #nameeroor가 뜬다


# In[51]:


get_ipython().run_line_magic('whos', '')


# In[52]:


#여기에 없는 애들이 NameError가 뜨는 것이다


# In[53]:


# %는 3개가 있다


# In[54]:


get_ipython().run_line_magic('who_ls', '')


# In[56]:


# 없으면 nameerror 있으면 그 결과값을 반환


# In[57]:


id(a)


# In[58]:


# 메모리 공간에 할당된 것이다


# In[59]:


hex(id(a))


# In[60]:


# 16진수. 이러한 메모리 공간에 할당이 된다


# In[61]:


b = 1000


# In[62]:


id(a)


# In[63]:


hex(id(b))


# In[64]:


# 정수(int)일 때, -5 ~ 256이면 똑같은 메모리 값을 가진다


# In[65]:


id(a)


# In[66]:


id(b)


# In[76]:


a = 1
c = 5


# In[77]:


id(c)


# In[78]:


id(a)


# In[79]:


hex(id(a))


# In[80]:


hex(id(b))


# In[70]:


id(b)


# In[71]:


from sys import intern


# In[72]:


# 다른 값이지만 똑같은 메모리 값에 들어가도록 하는 기법


# In[81]:


a == b


# In[82]:


id(a)


# In[83]:


id(b)


# In[84]:


a = 5


# In[85]:


id(a)


# In[86]:


b = 200


# In[87]:


id(b)


# In[88]:


a is b


# In[89]:


id(c)


# In[90]:


a == c


# In[91]:


a is c


# In[92]:


type(a)


# In[93]:


# 기본적으로 공부해야 할 타입은 13가지


# In[94]:


# a =1 하는 순간
# 1, 2는 앞에
# 3. type이 정해진다
# 4. pointing


# In[95]:


# 파이썬은 타입에 대한 힌트를 준다 -> literal
# 1. 객체방식 2. literal 방식


# In[96]:


# 정수는 literal에 아무것도 붙지 않을 때이다


# In[97]:


a = 1.


# In[98]:


type(a)


# In[99]:


# .을 붙이는 순간 literal이 된다


# In[101]:


a = .1


# In[102]:


type(a)


# In[103]:


# 정수는 float이 없다
# float에는 .과 e와 infinity와 NA값이 있다


# In[ ]:


# 왼쪽은 error가 나는 경우, error가 나지만 따라야 하는 경우
# 오른쪽은 식이 오는 경우

