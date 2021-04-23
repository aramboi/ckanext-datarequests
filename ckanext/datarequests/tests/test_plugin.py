# Copyright (c) 2015 CoNWeT Lab., Universidad Politécnica de Madrid

# This file is part of CKAN Data Requests Extension.

# CKAN Data Requests Extension is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# CKAN Data Requests Extension is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with CKAN Data Requests Extension. If not, see <http://www.gnu.org/licenses/>.

import unittest

from mock import MagicMock, patch
from nose_parameterized import parameterized

import ckanext.datarequests.constants as constants
import ckanext.datarequests.plugin as plugin

TOTAL_ACTIONS = 13
COMMENTS_ACTIONS = 5
ACTIONS_NO_COMMENTS = TOTAL_ACTIONS - COMMENTS_ACTIONS


class DataRequestPluginTest(unittest.TestCase):
    def setUp(self):
        self.actions_patch = patch("ckanext.datarequests.plugin.actions")
        self.actions_mock = self.actions_patch.start()

        self.auth_patch = patch("ckanext.datarequests.plugin.auth")
        self.auth_mock = self.auth_patch.start()

        self.tk_patch = patch("ckanext.datarequests.plugin.tk")
        self.tk_mock = self.tk_patch.start()

        self.config_patch = patch("ckanext.datarequests.plugin.config")
        self.config_mock = self.config_patch.start()

        self.helpers_patch = patch("ckanext.datarequests.plugin.helpers")
        self.helpers_mock = self.helpers_patch.start()

        self.partial_patch = patch("ckanext.datarequests.plugin.partial")
        self.partial_mock = self.partial_patch.start()

        self.h_patch = patch("ckanext.datarequests.plugin.h")
        self.h_mock = self.h_patch.start()

        self.create_datarequest = constants.CREATE_DATAREQUEST
        self.show_datarequest = constants.SHOW_DATAREQUEST
        self.update_datarequest = constants.UPDATE_DATAREQUEST
        self.list_datarequests = constants.LIST_DATAREQUESTS
        self.delete_datarequest = constants.DELETE_DATAREQUEST
        self.comment_datarequest = constants.COMMENT_DATAREQUEST
        self.list_datarequest_comments = constants.LIST_DATAREQUEST_COMMENTS
        self.show_datarequest_comment = constants.SHOW_DATAREQUEST_COMMENT
        self.update_datarequest_comment = constants.UPDATE_DATAREQUEST_COMMENT
        self.delete_datarequest_comment = constants.DELETE_DATAREQUEST_COMMENT
        self.follow_datarequest = constants.FOLLOW_DATAREQUEST
        self.unfollow_datarequest = constants.UNFOLLOW_DATAREQUEST

    def tearDown(self):
        self.actions_patch.stop()
        self.auth_patch.stop()
        self.tk_patch.stop()
        self.config_patch.stop()
        self.helpers_patch.stop()
        self.partial_patch.stop()
        self.h_patch.stop()

    @parameterized.expand([("True",), ("False",)])
    def test_get_actions(self, comments_enabled):

        actions_len = (
            TOTAL_ACTIONS if comments_enabled == "True" else ACTIONS_NO_COMMENTS
        )

        # Configure config and create instance
        plugin.config.get.return_value = comments_enabled
        self.plg_instance = plugin.DataRequestsPlugin()

        # Get actions
        actions = self.plg_instance.get_actions()

        self.assertEquals(actions_len, len(actions))
        self.assertEquals(
            plugin.actions.create_datarequest, actions[self.create_datarequest]
        )
        self.assertEquals(
            plugin.actions.show_datarequest, actions[self.show_datarequest]
        )
        self.assertEquals(
            plugin.actions.update_datarequest, actions[self.update_datarequest]
        )
        self.assertEquals(
            plugin.actions.list_datarequests, actions[self.list_datarequests]
        )
        self.assertEquals(
            plugin.actions.delete_datarequest, actions[self.delete_datarequest]
        )
        self.assertEquals(
            plugin.actions.follow_datarequest, actions[self.follow_datarequest]
        )
        self.assertEquals(
            plugin.actions.unfollow_datarequest, actions[self.unfollow_datarequest]
        )

        if comments_enabled == "True":
            self.assertEquals(
                plugin.actions.comment_datarequest, actions[self.comment_datarequest]
            )
            self.assertEquals(
                plugin.actions.list_datarequest_comments,
                actions[self.list_datarequest_comments],
            )
            self.assertEquals(
                plugin.actions.show_datarequest_comment,
                actions[self.show_datarequest_comment],
            )
            self.assertEquals(
                plugin.actions.update_datarequest_comment,
                actions[self.update_datarequest_comment],
            )
            self.assertEquals(
                plugin.actions.delete_datarequest_comment,
                actions[self.delete_datarequest_comment],
            )

    @parameterized.expand([("True",), ("False",)])
    def test_get_auth_functions(self, comments_enabled):

        auth_functions_len = (
            TOTAL_ACTIONS if comments_enabled == "True" else ACTIONS_NO_COMMENTS
        )

        # Configure config and create instance
        plugin.config.get.return_value = comments_enabled
        self.plg_instance = plugin.DataRequestsPlugin()

        # Get auth functions
        auth_functions = self.plg_instance.get_auth_functions()

        self.assertEquals(auth_functions_len, len(auth_functions))
        self.assertEquals(
            plugin.auth.create_datarequest, auth_functions[self.create_datarequest]
        )
        self.assertEquals(
            plugin.auth.show_datarequest, auth_functions[self.show_datarequest]
        )
        self.assertEquals(
            plugin.auth.update_datarequest, auth_functions[self.update_datarequest]
        )
        self.assertEquals(
            plugin.auth.list_datarequests, auth_functions[self.list_datarequests]
        )
        self.assertEquals(
            plugin.auth.delete_datarequest, auth_functions[self.delete_datarequest]
        )
        self.assertEquals(
            plugin.auth.follow_datarequest, auth_functions[self.follow_datarequest]
        )
        self.assertEquals(
            plugin.auth.unfollow_datarequest, auth_functions[self.unfollow_datarequest]
        )

        if comments_enabled == "True":
            self.assertEquals(
                plugin.auth.comment_datarequest,
                auth_functions[self.comment_datarequest],
            )
            self.assertEquals(
                plugin.auth.list_datarequest_comments,
                auth_functions[self.list_datarequest_comments],
            )
            self.assertEquals(
                plugin.auth.show_datarequest_comment,
                auth_functions[self.show_datarequest_comment],
            )
            self.assertEquals(
                plugin.auth.update_datarequest_comment,
                auth_functions[self.update_datarequest_comment],
            )
            self.assertEquals(
                plugin.auth.delete_datarequest_comment,
                auth_functions[self.delete_datarequest_comment],
            )

    def test_update_config(self):
        # Create instance
        self.plg_instance = plugin.DataRequestsPlugin()

        # Test
        config = MagicMock()
        self.plg_instance.update_config(config)
        plugin.tk.add_template_directory.assert_called_once_with(config, "templates")

    @parameterized.expand([("True",), ("False")])
    def test_before_map(self, comments_enabled):

        urls_set = 12
        mapa_calls = urls_set if comments_enabled == "True" else urls_set - 2

        # Configure config and get instance
        plugin.config.get.return_value = comments_enabled
        self.plg_instance = plugin.DataRequestsPlugin()

        mock_icon = "question-circle"
        # get_question_icon_patch = patch(
        #     "ckanext.datarequests.plugin.get_question_icon", return_value=mock_icon
        # )
        # get_question_icon_patch.start()
        # self.addCleanup(get_question_icon_patch.stop)

        # Test
        mapa = MagicMock()
        dr_basic_path = "datarequest"
        self.plg_instance.before_map(mapa)

        self.assertEquals(mapa_calls, mapa.connect.call_count)
        mapa.connect.assert_any_call(
            "datarequests_index",
            f"/{dr_basic_path}",
            controller="datarequests",
            action="index",
            conditions=dict(method=["GET"]),
        )

        mapa.connect.assert_any_call(
            f"/{dr_basic_path}/new",
            controller="datarequests",
            action="new",
            conditions=dict(method=["GET", "POST"]),
        )

        mapa.connect.assert_any_call(
            "show_datarequest",
            f"/{dr_basic_path}/{{id}}",
            controller="datarequests",
            action="show",
            conditions=dict(method=["GET"]),
            ckan_icon=mock_icon,
        )

        mapa.connect.assert_any_call(
            f"/{dr_basic_path}/edit/{{id}}",
            controller="datarequests",
            action="update",
            conditions=dict(method=["GET", "POST"]),
        )

        mapa.connect.assert_any_call(
            f"/{dr_basic_path}/delete/{{id}}",
            controller="datarequests",
            action="delete",
            conditions=dict(method=["POST"]),
        )

        mapa.connect.assert_any_call(
            f"/{dr_basic_path}/close/{{id}}",
            controller="datarequests",
            action="close",
            conditions=dict(method=["GET", "POST"]),
        )

        mapa.connect.assert_any_call(
            "organization_datarequests",
            f"/organization/{dr_basic_path}/{{id}}",
            controller="datarequests",
            action="organization_datarequests",
            conditions=dict(method=["GET"]),
            ckan_icon=mock_icon,
        )

        mapa.connect.assert_any_call(
            "user_datarequests",
            f"/user/{dr_basic_path}/{{id}}",
            controller="datarequests",
            action="user_datarequests",
            conditions=dict(method=["GET"]),
            ckan_icon=mock_icon,
        )

        mapa.connect.assert_any_call(
            "user_datarequests",
            f"/user/{dr_basic_path}/{{id}}",
            controller="datarequests",
            action="user_datarequests",
            conditions=dict(method=["GET"]),
            ckan_icon=mock_icon,
        )

        mapa.connect(
            f"/{dr_basic_path}/follow/{{id}}",
            controller="datarequests",
            action="follow",
            conditions=dict(method=["POST"]),
        )

        mapa.connect(
            f"/{dr_basic_path}/unfollow/{{id}}",
            controller="datarequests",
            action="unfollow",
            conditions=dict(method=["POST"]),
        )

        if comments_enabled == "True":
            mapa.connect.assert_any_call(
                "comment_datarequest",
                f"/{dr_basic_path}/comment/{{id}}",
                controller="datarequests",
                action="comment",
                conditions=dict(method=["GET", "POST"]),
                ckan_icon="comment",
            )

            mapa.connect.assert_any_call(
                f"/{dr_basic_path}/comment/{{datarequest_id}}/delete/{{comment_id}}",
                controller="datarequests",
                action="delete_comment",
                conditions=dict(method=["GET", "POST"]),
            )

    @parameterized.expand(
        [("True", "True"), ("True", "False"), ("False", "True"), ("False", "False")]
    )
    def test_helpers(self, comments_enabled, show_datarequests_badge):

        # Configure config and get instance
        plugin.config = {
            "ckan.datarequests.comments": comments_enabled,
            "ckan.datarequests.show_datarequests_badge": show_datarequests_badge,
        }
        self.plg_instance = plugin.DataRequestsPlugin()

        # Check result
        show_comments_expected = True if comments_enabled == "True" else False
        helpers = self.plg_instance.get_helpers()
        self.assertEquals(helpers["show_comments_tab"](), show_comments_expected)
        self.assertEquals(
            helpers["get_comments_number"], plugin.helpers.get_comments_number
        )
        self.assertEquals(
            helpers["get_comments_badge"], plugin.helpers.get_comments_badge
        )
        self.assertEquals(
            helpers["get_open_datarequests_number"],
            plugin.helpers.get_open_datarequests_number,
        )
        self.assertEquals(
            helpers["get_open_datarequests_badge"], plugin.partial.return_value
        )

        # Check that partial has been called
        show_datarequests_expected = (
            True if show_datarequests_badge == "True" else False
        )
        plugin.partial.assert_called_once_with(
            plugin.helpers.get_open_datarequests_badge, show_datarequests_expected
        )
