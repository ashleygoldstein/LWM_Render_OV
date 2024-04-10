import omni.ext
import omni.ui as ui
import omni.kit.actions.core

# ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[lwm.render.types] lwm render types startup")

        self.action_registry = omni.kit.actions.core.get_action_registry()

        self._window = ui.Window("LWM RENDER TYPES", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                label = ui.Label("Render Types")


                def real_time():
                    action = self.action_registry.get_action("omni.kit.viewport.actions", "set_renderer_rtx_realtime")
                    action.execute()

                def path_tracing():
                    action = self.action_registry.get_action("omni.kit.viewport.actions", "set_renderer_rtx_pathtracing")
                    action.execute()


                def iray():
                    action = self.action_registry.get_action("omni.kit.viewport.actions", "set_renderer_iray")
                    action.execute()                


                def storm():
                    action = self.action_registry.get_action("omni.kit.viewport.actions", "set_renderer_pxr_storm")
                    action.execute()

                with ui.HStack():
                    ui.Button("Real Time", clicked_fn=real_time)
                    ui.Button("Path Tracing", clicked_fn=path_tracing)
                    ui.Button("Iray", clicked_fn=iray)
                    ui.Button("Storm", clicked_fn=storm)

    def on_shutdown(self):
        print("[lwm.render.types] lwm render types shutdown")
