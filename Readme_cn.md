<a href="https://github.com/dizzyeyes/ProductRating">英文</a> <a href="https://github.com/dizzyeyes/ProductRating/blob/main/Readme_cn.md">中文</a> 

# ProductRating

对于京东plus会员，在商品评价之后会，京东会给予京豆奖励，但是需要评价字数至少40字。因此自动化的生成评价很有必要。

本项目使用智源的FlagAI模型，使用商品连接中的标题，生成一段正面或者负面的评价。

# 前提：

需要将<a href="https://model.baai.ac.cn/model-detail/100003">GLM-large-ch</a>模型下载到"./checkpoints/GLM-large-ch/"

将<a href="https://model.baai.ac.cn/model-detail/100078">AltDiffusion-m9</a>模型下载到"./checkpoints/AltDiffusion-m9/"

# 步骤：

  1. selenium登录京东账号 

  2. 跳转待评价页面 

  3. 获取商品标题 

  4. 使用flagai生成评价文字和图片 
  
    * 4.1 生成评价文字 ，使用GLM-large-ch模型
    
    * 4.2 生成图片，使用AltDiffusion-m9模型（未实现，显存需要较大）
    
  5. 提交 

  6. 进入下一个商品，循环2.


# Requirements 

pip install flagai

pip install pyppeteer

# 使用
双击运行 run.bat
