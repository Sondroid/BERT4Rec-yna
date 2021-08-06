def set_template(args):
    if args.template is None:
        return

    elif args.template.startswith('train_bert'):
        args.mode = 'train'

        args.dataset_code = 'yna'
        args.min_rating = 0 # ignore
        args.min_uc = 5
        args.min_sc = 2
        args.split = 'leave_one_out'

        args.dataloader_code = 'bert'
        batch = 2048
        args.train_batch_size = batch
        args.val_batch_size = batch
        args.test_batch_size = batch

        args.train_negative_sampler_code = 'random'
        args.train_negative_sample_size = 0
        args.train_negative_sampling_seed = 0
        args.test_negative_sampler_code = 'random'
        args.test_negative_sample_size = 100
        args.test_negative_sampling_seed = 98765

        args.trainer_code = 'bert'
        args.device = 'cuda'
        args.num_gpu = 1
        args.device_idx = '0'
        args.optimizer = 'Adam'
        args.lr = 0.0025
        args.enable_lr_schedule = True
        args.decay_step = 25
        args.gamma = 1.0
        args.num_epochs = 200
        args.metric_ks = [1, 5, 10, 20, 50, 100]
        args.best_metric = 'NDCG@5'

        args.model_code = 'bert'
        args.model_init_seed = 0

        args.bert_dropout = 0.25
        args.bert_hidden_units = 256 # embed size
        args.bert_mask_prob = 0.30
        args.bert_max_len = 12
        args.bert_num_blocks = 2
        args.bert_num_heads = 8