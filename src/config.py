# -*- coding:utf-8 -*-
# ! usr/bin/env python3
"""
Created on 31/03/2021 9:38
@Author: XINZHI YAO
"""


class args:
    def __init__(self):
        # self.data_path = 'H:/AGAC_NER/data/test_data.txt'
        self.train_data = '../data/train_input.txt'
        self.test_data = '../data/test_input.txt'

        self.label_file = '../data/label.txt'

        # fixme: biobert-base-cased
        # self.model_name = 'bert-base-cased'
        self.model_name = 'dmis-lab/biobert-base-cased-v1.1'
        self.do_lower_case = False

        self.unk_token = '[UNK]'
        self.seq_token = '[SEP]'
        self.cls_token = '[CLS]'

        self.batch_size = 2
        self.shuffle = True
        self.drop_last = False
        self.max_length = 128

        self.hidden_size = 768
        self.droupout_prob = 0.03
        # self.num_tags = 25
        # fixme: add [PAD]
        self.num_tags = 26

        self.learning_rate = 4e-5
        # sgd adam adamw
        self.optimizer = 'adam'
        self.weight_decay = 1e-5
        self.momentum = 0.05

        self.max_steps = 0
        self.num_train_epochs = 15
        self.gradient_accumulation_steps = 10
        self.warmup_steps = 10
        self.adam_epsilon = 1e-8

        self.logging_step = 20
        self.example_step = 10
        self.print_example = True
        self.log_save_path = '../logging'
        self.model_save_name = 'bert-crf.pkl'
        self.log_file = '../log.txt'
        self.save_log_file = False
