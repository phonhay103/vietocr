import hydra
from omegaconf import OmegaConf
from vietocr.model.trainer import Trainer
import wandb
from dotenv import load_dotenv
import shutil

@hydra.main(version_base="1.2", config_path="config", config_name='vgg-seq2seq')
def main(config):
    load_dotenv()
    config = OmegaConf.to_container(config, resolve=True)
    if config['force']:
        shutil.rmtree(config['dataset']['train_lmdb'])

    wandb.init(project=config['project'], name=config['name'])
    trainer = Trainer(config)
    trainer.train()
    wandb.finish()

if __name__ == '__main__':
    main()
