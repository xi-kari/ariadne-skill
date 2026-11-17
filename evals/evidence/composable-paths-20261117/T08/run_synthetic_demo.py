"""合成测试材料：虚构队列的本地登记演示；工具命令、UTC 时间和文件校验是真实执行记录。"""
import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
PYTHON = '/tmp/ariadne-review-310/bin/python'
TOOL = '/workspace/ariadne-behavior-runs/skill-final/scripts/forecast.py'
REGISTRY = ROOT / 'synthetic-registry'


def utc_now():
    return datetime.now(timezone.utc)


def stamp(value):
    return value.isoformat(timespec='seconds').replace('+00:00', 'Z')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


now = utc_now()
cutoff = stamp(now)
forecast_id = 'synthetic-queue-' + now.strftime('%Y%m%dT%H%M%S%fZ')
log = {
    'material_label': '合成测试材料：所有队列内容均为虚构；本文件记录真实本地命令及结果，不是现实队列证据。',
    'clock_source': 'datetime.now(timezone.utc)，读取执行环境的真实 UTC 时钟；未使用固定示例日期或回填日期。',
    'created_at': cutoff,
    'forecast_id': forecast_id,
    'events': [],
}


def save_log():
    (ROOT / 'execution.json').write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_new(path, value):
    with path.open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    saved = json.loads(path.read_text(encoding='utf-8'))
    assert saved == value
    log['events'].append({'operation': 'write_and_read_back', 'path': str(path), 'sha256': digest(path.read_bytes())})
    save_log()


def run_tool(*args, receipt=None):
    command = [PYTHON, TOOL, *[str(arg) for arg in args]]
    started = stamp(utc_now())
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    log['events'].append({'operation': 'forecast_tool', 'command': command, 'cwd': str(ROOT), 'started_at': started, 'completed_at': stamp(utc_now()), 'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr})
    save_log()
    print(json.dumps(log['events'][-1], ensure_ascii=False), flush=True)
    if result.returncode:
        raise RuntimeError('forecast.py 调用失败；真实结果已保留在 execution.json。')
    parsed = json.loads(result.stdout)
    if receipt:
        with receipt.open('x', encoding='utf-8') as stream:
            stream.write(result.stdout)
        assert json.loads(receipt.read_text(encoding='utf-8')) == parsed
        log['events'].append({'operation': 'save_raw_tool_receipt', 'material_label': '合成测试流程的真实工具回执，原样保存。', 'path': str(receipt), 'sha256': digest(receipt.read_bytes())})
        save_log()
    return parsed


draft = {
    'artifact_version': '1.0',
    'artifact_type': 'forecast_draft',
    'forecast_id': forecast_id,
    'outcome_known': False,
    'model': {'id': 'synthetic-manual-queue-rule', 'version': '1'},
    'target': {
        'question': '【合成测试】虚构队列在截止时的未处理项目数是否严格超过 100？',
        'scope': '仅指 synthetic-fictional-queue-T08 这一虚构队列，统计未处理项目数；队列身份和统计口径保持不变。本测试不包含任何真实队列。',
        'outcome_rule': '仅使用截止瞬间、同一身份和口径的明确合成结果标签 N：整数 N > 100 为是，N <= 100 为否；缺失结果保留 null，不填零，不用当前假设 80 代替未来结果。',
    },
    'input': {
        'cutoff': cutoff,
        'sources': [{'source_id': 'synthetic-assumed-80', 'description': '合成测试材料：用户提供的唯一假设快照为 80 个未处理项目，未被现实观测证实。此 available_at 为本轮采纳该假设的真实 UTC 时间。没有流入、服务、历史频率或概率数据。', 'kind': 'assumption', 'available_at': cutoff}],
    },
    'window': {
        'starts_at': stamp(now + timedelta(hours=1)),
        'deadline': stamp(now + timedelta(hours=24)),
        'error_tolerance': '合成测试使用截止时的精确整数计数，阈值无容差；恰好 100 不属于超过 100。缺少对应时点标签时保留缺失，不作插值。',
    },
    'baseline': {
        'as_of': cutoff,
        'description': '合成测试的简单持平基线：当前假设计数持续不变；这只是冻结的比较规则，不是现实预测。',
        'expectation': '截止时仍为 80，故按该基线不超过 100。',
        'evaluation_rule': '若以后提供符合口径的合成标签 N，记录 N - 80 和 abs(N - 80)，以及阈值判断是否一致；无标签则比较不可评价。',
    },
    'mechanisms': [{'candidate_id': 'synthetic-balance', 'claim': '合成条件候选：若从假设快照到截止时累计流入恰好等于累计移出，且无其他计数变化，则计数保持 80。流量平衡仅是假设，尚无数据支持其发生。', 'basis_source_ids': ['synthetic-assumed-80']}],
    'paths': [{'path_id': 'synthetic-stable', 'description': '合成条件路径：80 → 在净增为零的额外条件下 → 截止仍为 80，不超过 100。本路径没有概率、权重或优先排序。', 'mechanism_ids': ['synthetic-balance'], 'basis_source_ids': ['synthetic-assumed-80']}],
    'competition_search': {
        'search_scope': '仅搜索用户提供的合成快照 80 及计数恒等关系；检查流入、移出、趋势、故障等是否有材料支撑，不作外部数据查询。',
        'reason_no_alternative': '只有一个静态假设数值，没有足以指定第二个完整机制或路径的流量及事件材料；保留上述持平条件候选作为演示，不声称它较可能或穷尽未来，净增与净减均未被排除。',
        'failure_conditions': '累计流入与移出不平衡即使持平路径不成立；净增超过 20 时阈值结果翻转。身份、统计口径变化会破坏目标条件。',
    },
    'expression': {'kind': 'unknown', 'reason': '合成测试只有假设快照 80，不能支持概率、信念数值、权重、方向判断或路径排序；明确弃权，不作可计为命中或失败的正负预测。'},
    'decision_use': {'status': 'not_applicable', 'reason': '合成测试仅演示本地登记、原件验证和一次缺失标签追加，不用于现实决策。'},
    'evaluation': {
        'rule': '按冻结的 N > 100 规则记录未来明确合成标签；unknown 表达不评分。目标标签、基线比较及预测可评价性分别保留，缺失标签不是零。',
        'calibration_plan': '本合成测试不声称概率校准或预测能力。保留全部登记和追加历史；如以后汇总，应报告总登记数、unknown 弃权数、缺失标签数与实际可评价数，本条不进入预测命中率或概率评分分母。',
        'failure_rules': {
            'supported': '本条 unknown 表达不适用；即使后来提供超过 100 的合成标签，也不能计为预测命中。',
            'not_supported': '本条 unknown 表达不适用；弃权不计为正负预测失败。',
            'unresolved': '合成标签存在冲突或不足以确定同一目标结果时，保留争议和缺口。',
            'target_invalid': '虚构队列身份或统计口径变更，使原目标不再指向同一对象；保留原件。',
            'not_evaluable': '本条原始表达明确弃权；未取得标签时 actual_result 为 null，基线也不可评价；后续任何合成结果与弃权评分分别记录。',
        },
    },
    'signals': {
        'early': ['合成测试中若以后获得独立记录的到达批次或处理能力变化，可用来检查流量平衡条件；目前未得到这些记录。'],
        'reverse': ['合成测试中若累计流入与移出出现非零差额，持平条件即被推翻；目前没有这类标签。'],
        'pause': ['缺少同一口径的截止标签时暂停结果判定；任何将合成假设当作现实证据的使用均不在本测试范围内。'],
        'retirement': ['虚构队列身份或统计口径被替换时停用该目标；需另建新 ID 并保留旧登记。'],
    },
    'response_regime': '合成测试仅在本目录写入和验证文件，不发布到外部，不触发现实队列干预；工具执行成功不证明队列机制或预测能力。',
    'review': {
        'owner': '本轮执行助手：负责登记后立即进行一次缺失标签检查及追加，最迟在 next_review_at 前完成；本轮不安排无人值守的截止复查。',
        'next_review_at': stamp(now + timedelta(minutes=10)),
        'writeback_due_at': stamp(now + timedelta(hours=25)),
        'destination': str(REGISTRY / forecast_id / 'resolutions') + '；仅追加新记录，原件不重写。writeback_due_at 是本合成合同的截止后边界，不代表已安排未来后台任务。',
    },
}

draft_path = ROOT / 'synthetic-draft.json'
write_new(draft_path, draft)
run_tool('validate', draft_path)
receipt = run_tool('register', '--input', draft_path, '--registry', REGISTRY, receipt=ROOT / 'synthetic-registration-receipt.json')
original_path = REGISTRY / forecast_id / 'forecast.json'
original_bytes = original_path.read_bytes()
original_hash = digest(original_bytes)
registered = json.loads(original_bytes)
assert receipt['sha256'] == original_hash
assert receipt['readback_verified'] is True
assert registered['expression']['kind'] == 'unknown'
assert registered['outcome_known'] is False
assert registered['target'] == draft['target']
run_tool('validate', original_path)

observation = {
    'artifact_version': '1.0',
    'artifact_type': 'resolution_draft',
    'resolution_id': 'synthetic-missing-label-1',
    'observed_at': stamp(utc_now()),
    'sources': [],
    'actual_result': None,
    'status': 'not_evaluable',
    'reason': '合成测试的登记后检查：截止时间仍在未来，尚未提供任何截止结果标签；sources 为空，因为没有结果来源。原登记 expression 为 unknown。此记录只陈述本轮标签缺失，不是现实队列观察，也不是最终结果判定。',
    'baseline_comparison': '合成测试基线仍冻结为 80；因 actual_result 为 null，差值、绝对误差和阈值比较均不可评价，不能填 0 或沿用假设 80 作为结果。',
    'response_observations': '本轮只执行本地文件登记与缺失标签追加，无现实干预，也无虚构结果标签生成。',
    'next_step': '本轮演示在验证本次追加及原件完整性后结束。若用户以后提供明确的合成截止标签，手动调用 resolve 并使用新的 resolution_id 追加；unknown 仍不能计为预测命中。不承诺后台监控或自动复查。',
}
observation_path = ROOT / 'synthetic-observation.json'
write_new(observation_path, observation)
run_tool('validate', observation_path)
resolution_receipt = run_tool('resolve', '--id', forecast_id, '--input', observation_path, '--registry', REGISTRY, receipt=ROOT / 'synthetic-resolution-receipt.json')
resolution_path = original_path.parent / 'resolutions' / 'synthetic-missing-label-1.json'
run_tool('validate', resolution_path)
run_tool('validate', original_path)

resolution_bytes = resolution_path.read_bytes()
resolution = json.loads(resolution_bytes)
assert original_path.read_bytes() == original_bytes
assert digest(original_path.read_bytes()) == original_hash == receipt['sha256']
assert resolution['registered_artifact_sha256'] == original_hash
assert resolution_receipt['sha256'] == digest(resolution_bytes)
assert resolution_receipt['readback_verified'] is True
assert resolution['actual_result'] is None
assert resolution['status'] == 'not_evaluable'
assert resolution['sources'] == []
assert len(list((original_path.parent / 'resolutions').glob('*.json'))) == 1
parse = lambda value: datetime.fromisoformat(value.replace('Z', '+00:00'))
assert parse(cutoff) <= parse(registered['registered_at']) < parse(draft['window']['starts_at']) < parse(draft['window']['deadline'])
assert parse(resolution['observed_at']) <= parse(resolution['resolved_at']) < parse(draft['review']['next_review_at'])
verification = {
    'material_label': '合成测试材料的真实文件与流程核验；不认证任何现实队列事实。',
    'forecast_id': forecast_id,
    'cutoff': cutoff,
    'registered_at': registered['registered_at'],
    'window': draft['window'],
    'original_artifact': str(original_path),
    'original_sha256_before_append': original_hash,
    'original_sha256_after_append': digest(original_path.read_bytes()),
    'original_bytes_unchanged': True,
    'registration_receipt_hash_matches': True,
    'resolution_receipt_hash_matches': True,
    'resolution_binds_original_hash': True,
    'resolution_artifact': str(resolution_path),
    'resolution_count': 1,
    'expression': 'unknown',
    'resolution_status': resolution['status'],
    'actual_result': resolution['actual_result'],
    'outcome_source_count': len(resolution['sources']),
    'tool_validation_count': 5,
    'future_window_verified': True,
    'immediate_review_completed_at': resolution['resolved_at'],
    'background_monitoring': False,
}
write_new(ROOT / 'synthetic-verification.json', verification)
log['completed_at'] = stamp(utc_now())
log['completion'] = verification
save_log()
print(json.dumps(verification, ensure_ascii=False, indent=2))
