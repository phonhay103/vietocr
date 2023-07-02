import hydra
from omegaconf import OmegaConf
from vietocr.model.trainer import Trainer

@hydra.main(version_base="1.2", config_path="config", config_name='vgg-seq2seq')
def main(config):
    config = OmegaConf.to_container(config, resolve=True)
    sample = config['trainer']['metrics']
    weight = config['trainer']['export']

    trainer = Trainer(config)
    trainer.load_weights(weight)
    
    print('valid:', trainer.precision(sample))
    print('test:', trainer.test_precision(sample))

if __name__ == '__main__':
    main()