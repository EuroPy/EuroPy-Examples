import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten
from transformers import TFBertModel

class BertClassifier(tf.keras.Model):
    def __init__(self, bert: TFBertModel, num_classes: int):
        super().__init__()
        self.bert = bert
        self.classifier = Dense(num_classes, activation='sigmoid')
        
    @tf.function
    def call(self, input_ids, attention_mask=None, token_type_ids=None, position_ids=None, head_mask=None):
        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask
        )
        
        cls_output = outputs[1]
        cls_output = self.classifier(cls_output)
        
        return cls_output