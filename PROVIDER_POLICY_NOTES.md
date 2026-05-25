# Provider Policy Notes

The public benchmark is designed around safe evaluation practice:

- use official provider APIs only
- use benign synthetic or public-domain scenarios
- respect provider usage policies and rate limits
- cache or retain only artifacts appropriate for public review
- redact sensitive inputs and outputs
- do not publish harmful prompts, harmful outputs, or safeguard-bypass techniques

Provider-backed results should record the provider, model identifier, model/version date when available, evaluation date, suite version, and material configuration changes.

The OpenAI and Anthropic adapters in this repository are intentionally narrow interfaces. Provider-specific policy, authentication, data retention, and deployment decisions remain the responsibility of the operator.
