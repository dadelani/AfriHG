import rouge_scorer, scoring

def evaluate_rouge(predictions, targets, use_stemmer=True, use_aggregator=True, language="english"):
    """
    Evaluates ROUGE scores for given predictions and targets.

    Args:
        predictions (list): List of predicted text strings.
        targets (list): List of ground truth text strings.
        use_stemmer (bool): Whether to use stemming.
        use_aggregator (bool): Whether to aggregate results.
        language (str): Language code for the text (e.g., "english", "arabic").

    Returns:
        dict: ROUGE scores (mean F1) for each metric.
    """
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=use_stemmer, lang=language)
    
    if use_aggregator:
        aggregator = scoring.BootstrapAggregator()
        for prediction, target in zip(predictions, targets):
            scores = scorer.score(prediction, target)
            aggregator.add_scores(scores)
        aggregated_scores = aggregator.aggregate()
        return {key: value.mid.fmeasure for key, value in aggregated_scores.items()}
    else:
        results = [scorer.score(prediction, target) for prediction, target in zip(predictions, targets)]
        return results
