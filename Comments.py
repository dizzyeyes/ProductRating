#
# Licensed under the Apache License, Version 2.0 (the "License")
from flagai.auto_model.auto_loader import AutoLoader
from flagai.model.predictor.predictor import Predictor
import torch 


def comments_gen(title):
    loader = AutoLoader(task_name="lm",
                        model_name="GLM-large-ch",
                        )
    model = loader.get_model().half()
    tokenizer = loader.get_tokenizer()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    predictor = Predictor(model, tokenizer)
    text = "问题：请写一个正面的购物评价，要求40字“{}”？回答：[gMASK]".format(title)
    pos_output=predictor.predict_generate_randomsample(text, top_k=50, repetition_penalty=4.0, top_p=1.0)
    
    text = "问题：请写一个负面的购物评价，要求40字“{}”？回答：[gMASK]".format(title)
    neg_output=predictor.predict_generate_randomsample(text, top_k=50, repetition_penalty=4.0, top_p=1.0)
    return pos_output,neg_output
    
if __name__ == '__main__':
    text = "惠寻 京东自有品牌 抽绳垃圾袋45只自动收口加厚塑料袋大号垃圾桶袋Y"
    print(comments_gen(text))