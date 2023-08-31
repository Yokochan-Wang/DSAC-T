from utils.sys_run import PolicyRunner

runner = PolicyRunner(
    log_policy_dir_list=["./results/230831-224040"],
    trained_policy_iteration_list=["7800_opt"],
    is_init_info=False,
    init_info={"init_state": [-1, 0.05, 0.05, 0, 0.1, 0.1]},
    save_render=True,
    legend_list=["DSAC"],
    dt=0.01, # time interval between steps
)

runner.run()
