from transformers import AutoConfig
from transformers.models.aimv2.configuration_aimv2 import AIMv2Config

AutoConfig.register("aimv2", AIMv2Config, exist_ok=True)
